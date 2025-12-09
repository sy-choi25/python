import os
import warnings
from dotenv import load_dotenv
from typing import List, Tuple
import hashlib

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.retrievers import TavilySearchAPIRetriever, BM25Retriever
from langchain_core.documents import Document


from enum import Enum
from pydantic import BaseModel

warnings.filterwarnings("ignore")
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY 없음! .env 확인해줘")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY") 

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

# 벡터DB 로드

# 1) 메인 문서용 벡터DB
vectorstore = Chroma(
    persist_directory="./chroma_startup_all",
    collection_name="startup_all_rag",
    embedding_function=embedding_model,
)

# 2) 캐시 전용 벡터DB 
cache_vectorstore = Chroma(
    persist_directory="./chroma_cache",
    collection_name="semantic_cache",
    embedding_function=embedding_model,
)

# 백터스토어 상태 확인 함수
def check_vectorstore(name, store):
    try:
        data = store.get()
        ids = data.get("ids", [])
        print(f"{name} 로드 완료 / 총 개수: {len(ids)}")
        return len(ids) > 0
    except Exception as e:
        print(f"⚠ {name} 상태 확인 중 에러:", e)
        return False

main_db_ok = check_vectorstore("메인 벡터DB", vectorstore)
cache_db_ok = check_vectorstore("캐시 벡터DB", cache_vectorstore)

# ========================================
# 하이브리드 리트리버 구현
# ========================================

class HybridRetriever:
    """Dense(의미) + BM25(키워드) 하이브리드 리트리버"""
    
    def __init__(self,
        vectorstore: Chroma,
        documents: List[Document],
        k: int = 10,    #-> 검색 후 최종적으로 반환할 문서
        dense_weight: float = 0.6,  # 의미기반 비중
        bm25_weight: float = 0.4,): # 키워드기반 비중
        # 파라미터 저장
        self.vectorstore = vectorstore
        self.k = k
        self.dense_weight = dense_weight
        self.bm25_weight = bm25_weight
        self._internal_k = k * 2  # 더 많이 가져온 후 융합( 최종 반환은 10개이고 내부에서는 그것보다 더 많이 가져와서 비교 후 10개만 반환)
        
        # Dense retriever -> 벡터스토어 기반 형태 필요
        self.dense_retriever = vectorstore.as_retriever(
            search_kwargs={"k": self._internal_k}
        )
        
        # BM25 retriever -> documents 리스트 형태 필요
        print(f"[하이브리드] BM25 인덱스 생성 중... (문서 수: {len(documents)})")
        self.bm25_retriever = BM25Retriever.from_documents(documents)
        self.bm25_retriever.k = self._internal_k
        print(f"[하이브리드] BM25 인덱스 생성 완료")
    
    def invoke(self, query: str) -> List[Tuple[Document, float]]:
        """하이브리드 검색 실행 (RRF 융합)"""
        # Dense 검색
        dense_docs = self._search_dense(query)  # 메서드 앞에 붙은 _는 내부 전용이라는 뜻. 외부에서 직접 호출 안됨
        # BM25 검색
        bm25_docs = self._search_bm25(query)
        # RRF로 융합
        fused_docs = self._fuse_results(dense_docs, bm25_docs)
        
        return fused_docs[:self.k]  # internal_k * 2 개를 쓴 뒤,최종적으로 지정한 k만 반환
    
    def _search_dense(self, query: str) -> List[Document]:
        """Dense 검색""" # -> 벡터스토어 기반 검색
        try:
            return self.dense_retriever.invoke(query)
        except Exception as e:
            print(f"⚠ Dense 검색 오류: {e}")
            return []
    
    def _search_bm25(self, query: str) -> List[Document]:
        """BM25 검색""" # -> bm25 인덱스만 검색
        try:
            return self.bm25_retriever.invoke(query)    # 이 식에서 bm25 계산이 모두 이루어짐
        except Exception as e:
            print(f"⚠ BM25 검색 오류: {e}")
            return []
    
    def _fuse_results(self, dense_docs: List[Document],  bm25_docs: List[Document]) -> List[Tuple[Document, float]]:
        """RRF(Reciprocal Rank Fusion)로 검색 결과 통합"""
        scores = {}
        doc_map = {}
        
        # RRF 공식 = 1/ (rank +1)  -> 랭크가 뒤인거는 앞에 있는 것보다 차이를 더 많이 나게 하려고
        # Dense 점수 계산
        for rank, doc in enumerate(dense_docs): # dense_docs 리스트 순서를 rank로 바꿔준다
            key = self._get_doc_key(doc) # 문서를 고유하게 나타내는 값 dict의 key로 쓰기 위해 필요
            scores[key] = scores.get(key, 0.0) + self.dense_weight / (rank + 1) # 순위 기반 점수 계산식/ dense_weight(예: 0.6)이 곱해지면서 Dense 검색 영향력을 반영
            doc_map[key] = doc  # 점수는 scores에 저장되고, 문서 자체는 doc_map에 저장
        
        # BM25 점수 계산
        for rank, doc in enumerate(bm25_docs):
            key = self._get_doc_key(doc)
            scores[key] = scores.get(key, 0.0) + self.bm25_weight / (rank + 1)
            doc_map[key] = doc
        
        # 점수 기준 정렬
        ranked_keys = sorted(scores.keys(), key=lambda k: scores[k], reverse=True)  # lambda k: scores[k] -> def k:
                                                                                    #                            return scores[k]   -> 이것과 같은 의미
        # (Document, score) 형태로 반환
        return [(doc_map[k], scores[k]) for k in ranked_keys]
    
    @staticmethod   # 클래스 내부에서 쓰지만 self 필요없음
    def _get_doc_key(doc: Document) -> str:
        """문서 식별용 키 생성 (해시 기반)"""
        content_hash = hashlib.md5(doc.page_content[:500].encode()).hexdigest() # 해시생성은 500자만으로도 문서구별 충분
        return content_hash                                                     # encode-> 해시 함수는 바이트만 받음


# 하이브리드 리트리버 초기화
print("\n[초기화] 하이브리드 리트리버 생성 중...")
hybrid_retriever = None
if main_db_ok:
    try:
        all_docs_data = vectorstore.get(include=['documents', 'metadatas'])
        all_documents = [
            Document(page_content=doc, metadata=meta or {})
            for doc, meta in zip(
                all_docs_data.get('documents', []),
                all_docs_data.get('metadatas', [])
            )
        ]
        
        if len(all_documents) > 0:
            hybrid_retriever = HybridRetriever(
                vectorstore=vectorstore,
                documents=all_documents,
                k=10,
                dense_weight=0.6,
                bm25_weight=0.4
            )
            print("[초기화] 하이브리드 리트리버 준비 완료!\n")
        else:
            print("⚠ 문서가 없어 하이브리드 리트리버를 생성할 수 없습니다.")
    except Exception as e:
        print(f"⚠ 하이브리드 리트리버 생성 실패: {e}")
        print("⚠ Dense 리트리버만 사용합니다.")

# ========================================
# 캐시 시스템 (분리된 벡터DB 사용)
# ========================================

class SimpleCache:
    """L1 캐시 - 완전 일치 기반 메모리 캐시""" # 가장 안 쓰인 키 자동 삭제버전
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size        # 크기 제한
        self.access_count = {}          # 접근 횟수 제한

    def get(self, key):
        if key in self.cache:
            self.access_count[key] = self.access_count.get(key, 0) + 1
            print(f" [L1 캐시 히트] key: {key[:50]}...")
            return self.cache[key]
        return None
    
    def set(self, key, value):
        # LFU 기반 캐시 제거 -> 캐시를 일정한 크기 안에서 유지하고, 가장 덜 사용된 키를 자동을 제거
        if len(self.cache) >= self.max_size:
            if self.access_count:
                least_used = min(self.access_count, key=self.access_count.get)  # key=self.access_count.get -> 각 key의 valuse를 가져오는 값
                del self.cache[least_used]  # 캐시에 저장된 실제 값(value) 을 삭제
                del self.access_count[least_used]   # 해당 key의 접근 횟수 기록 삭제
        
        self.cache[key] = value     # 캐시에 값 저장
        self.access_count[key] = 0  # 캐시 접근 횟수 카운팅

    def stats(self):
        return {
            "size": len(self.cache),
            "max_size": self.max_size,
            "total_accesses": sum(self.access_count.values())
        }


class SemanticCache:
    """L2 캐시 - 의미적 유사도 기반 캐시 (분리된 캐시 전용 벡터DB 사용)
    DB에서 유사한 ID를 찾고, 그 ID로 메모리 캐시엣 실제 답변을 가져오는 구조"""
    
    def __init__(self, cache_vectorstore: Chroma, similarity_threshold=0.85):
        self.cache_vectorstore = cache_vectorstore  # 캐시 전용 DB
        self.similarity_threshold = similarity_threshold
        self.cache_data = {}  # {cache_id: response}
        self.cache_metadata = {}  # {cache_id: {query, timestamp, hits}}
        self._load_existing_cache()  # 프로그램 시작 시 DB에 있는 캐시를 메모리로 불러오는 것
        
    
    def _load_existing_cache(self):
        """기존 캐시 데이터 로드"""
        try:
            existing = self.cache_vectorstore.get(include=['metadatas'])
            for meta in existing.get('metadatas', []):
                cache_id = meta.get('cache_id') # 각 메타데이터 항목에서 캐시 고유 ID 가져오기/ ID가 존재하면 → 메모리에 저장 가능
                if cache_id:    # 만약 DB 데이터가 이상해서 cache_id가 없으면 저장하지 않음. 안전장치
                    self.cache_metadata[cache_id] = meta    # cache_id를 키로 해서 메타데이터 전체를 메모리에 저장
            print(f"[L2 캐시] 기존 캐시 {len(self.cache_metadata)}개 복구")
        except Exception as e:
            print(f"⚠ 캐시 복구 중 오류: {e}")
    
    def get(self, query: str):
        """유사한 질문이 캐시에 있으면 반환"""
        try:
            # 캐시 전용 DB에서 유사도 검색
            similar_docs = self.cache_vectorstore.similarity_search_with_score(query, k=1)  # 캐시 전용 벡터 DB(Chroma)에서 가장 유사한 1개 문서 검색
            
            if similar_docs:
                doc, distance = similar_docs[0] # 유사도가 가장 높은 0번째 문서를 가져온 것
                # Chroma distance -> 유사도 변환
                similarity = max(0.0, 1.0 - (distance / 2.0))
                
                if similarity >= self.similarity_threshold: # 유사도가 임계값 이상일 때
                    cache_id = doc.metadata.get('cache_id') # 문서의 메타데이터 고유ID(cache_id) 가져오기
                    
                    # 전체 응답 반환 (메타데이터가 아닌 실제 캐시 데이터에서)
                    if cache_id in self.cache_data:
                        full_response = self.cache_data[cache_id]
                        # L2캐시는 검색 결고와 실제 응답을 분리한다/검색 -> DB, 실제응답 -> 메모리
                        
                        # 캐시 히트 카운트 증가
                        if cache_id in self.cache_metadata:
                            self.cache_metadata[cache_id]['hits'] = \
                                self.cache_metadata[cache_id].get('hits', 0) + 1
                        
                        print(f"[L2 캐시 히트] 유사도: {similarity:.3f}, cache_id: {cache_id}")
                        return full_response
                    else:
                        print(f"⚠ [L2 경고] cache_id {cache_id}가 cache_data에 없음")

            return None
        except Exception as e:
            print(f"⚠ L2 캐시 검색 오류: {e}")
            return None
    
    def set(self, query: str, response: str):
        """질문과 응답을 캐시에 저장"""
        try:
            import time
            # 고유 ID 생성 -> 형식은 cache_메모리_인덱스_현재타임스탬프
            cache_id = f"cache_{len(self.cache_data)}_{int(time.time())}"
            
            # 전체 응답을 cache_data에 저장
            self.cache_data[cache_id] = response
            
            # 메타데이터 저장 (요약본만)
            metadata = {
                'cache_id': cache_id,
                'response_preview': response[:200] + "..." if len(response) > 200 else response,
                'timestamp': time.time(),
                'hits': 0
            }
            self.cache_metadata[cache_id] = metadata
            
            # 캐시 전용 벡터DB에 저장
            self.cache_vectorstore.add_texts(
                texts=[query],
                metadatas=[metadata],
                ids=[cache_id]
            )
            self.cache_vectorstore.persist()

            print(f"[L2 캐시 저장] cache_id: {cache_id}, 응답 길이: {len(response)}자")
        except Exception as e:
            print(f"⚠ L2 캐시 저장 오류: {e}")
    
    def stats(self):
        return {
            "size": len(self.cache_data),
            "total_hits": sum(m.get('hits', 0) for m in self.cache_metadata.values()),
            "avg_hits": sum(m.get('hits', 0) for m in self.cache_metadata.values()) / max(len(self.cache_metadata), 1)
        }


class MultiLevelCache:
    """멀티레벨 캐시 - L1(완전일치) + L2(의미적 유사도)"""
    
    def __init__(self, cache_vectorstore: Chroma):
        self.l1_cache = SimpleCache(max_size=100)
        self.l2_cache = SemanticCache(
            cache_vectorstore=cache_vectorstore,
            similarity_threshold=0.85
        )
        self.stats_data = {
            'l1_hits': 0,
            'l2_hits': 0,
            'misses': 0
        }
    
    def get(self, key: str, execute_rag_callable):
        """캐시 조회 > 내부문서 > 웹서치 > LLM 호출 순서"""
        # L1 캐시 확인
        cached = self.l1_cache.get(key)
        if cached:
            self.stats_data['l1_hits'] += 1
            print(' L1 cache hit')
            return cached
    
        # L2 캐시 확인
        cached = self.l2_cache.get(key)
        if cached:
            self.stats_data['l2_hits'] += 1
            print(' L2 cache hit')
            self.l1_cache.set(key, cached)
            return cached
                

        # 캐시 미스 → execute_rag() 호출
        self.stats_data['misses'] += 1
        print('❌ [캐시 미스] RAG 파이프라인 실행')
        response = execute_rag_callable(key)# execute_rag 안에서 QT → MQ → 내부 문서 검색 → 유사도 필터링 → 관련성 검증 → 웹 → LLM 수행

        # 결과를 L1/L2 캐시에 저장
        self.l1_cache.set(key, response)
        self.l2_cache.set(key, response)
        print("[캐시 저장 완료]\n")
         
        return response
        
    def stats(self):
        total = sum(self.stats_data.values())
        hit_rate = (self.stats_data['l1_hits'] + self.stats_data['l2_hits']) / max(total, 1) * 100
        
        print("\n" + "="*60)
        print("📊 캐시 통계")
        print("="*60)
        print(f"L1 히트: {self.stats_data['l1_hits']}")
        print(f"L2 히트: {self.stats_data['l2_hits']}")
        print(f"캐시 미스: {self.stats_data['misses']}")
        print(f"총 요청: {total}")
        print(f"캐시 히트율: {hit_rate:.1f}%")
        print(f"\nL1 상세: {self.l1_cache.stats()}")
        print(f"L2 상세: {self.l2_cache.stats()}")
        print("="*60 + "\n")

# ========================================
# 프롬프트 정의
# ========================================

# 관련성 검증 프롬프트
relevance_check_prompt = ChatPromptTemplate.from_template("""
당신은 문서와 질문의 관련성을 엄격하게 판단하는 전문가입니다.

[질문]
{question}

[검색된 문서 샘플]
{documents}

[판단 기준]
1. 질문의 핵심 주제와 문서의 내용이 직접적으로 관련되는가?
2. 문서가 질문에 대한 구체적인 정보를 제공하는가?
3. 단순히 유사한 단어가 있는 것이 아니라, 실제 답변 가능한 내용인가?

[예시]
- "서울 동물병원" vs "서울 창업 공간" → 관련없음 (서울만 공통)
- "AI 교육" vs "창업 교육" → 관련없음 (교육만 공통, 주제 다름)
- "창업 지원사업" vs "창업 자금 지원" → 관련있음 (직접 연관)

다음 중 하나로만 답변: "관련있음" 또는 "관련없음"

답변:""")

# Query Transformation
qt_prompt = ChatPromptTemplate.from_template("""
다음 사용자 질문을 벡터 검색에 적합한 '핵심 키워드 중심 문장'으로 바꾸세요.
불필요한 말은 제거하고, 핵심 조건만 남기세요.

원본 질문: {question}

변환된 검색용 문장:""")

# 멀티쿼리 생성
multi_query_prompt = ChatPromptTemplate.from_template("""
다음질문에 대해 3가지 다른 관점의 검색 쿼리를 생성하세요.
각쿼리는 세 줄로 구분하여 출력하세요        
번호나 설명 없이 쿼리만 출력하세요

원본질문: {question}""")

# 기본 RAG 프롬프트
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", """
당신은 예비·초기 창업자를 도와주는 '창업 지원 통합 AI 어시스턴트'입니다.

[사용 가능한 정보 유형]
- 지원사업 공고 (announcement)
- 실패/재도전 사례 (cases)
- 창업 공간 정보 (space)
- 법령: 중소기업창업 지원법 등 (law)
- 통계, 매뉴얼 등 참고 자료

[답변 원칙]
1. 반드시 제공된 문맥(Context) 안의 정보만 사용하세요.
2. 문맥에 없는 내용은 추측하지 말고 솔직하게 말하세요.
3. 질문 성격에 따라 다음 정보 유형을 우선 활용하세요.
   - 지원사업·신청 가능 여부 → announcement
   - 법적 정의·자격 요건 → law
   - 조언·주의점 → cases
   - 공간·입주 → space
4. 핵심 답변 후 필요하면 bullet로 정리하세요.
5. 마지막에 참고 근거 유형을 요약하세요.
"""),
    ("human", "[문맥]\n{context}\n\n[질문]\n{question}\n\n[답변]")
])

# 법령 전용 프롬프트
law_prompt = ChatPromptTemplate.from_messages([
    ("system", """
당신은 중소기업창업 지원법을 바탕으로 창업 제도와 요건을 설명하는 AI입니다.

[규칙]
1. 반드시 문맥에 있는 법령 내용만 사용하세요.
2. 가능하면 조문 번호(제○조)를 함께 제시하세요.
3. 문맥에 없는 내용은 "제공된 법령 문서에서 해당 내용은 확인되지 않습니다."라고 답하세요.
4. 답변 끝에 "※ 본 답변은 일반 정보 제공이며, 구체적인 법률 자문은 아닙니다."를 포함하세요.
"""),
    ("human", "[법령 문맥]\n{context}\n\n[질문]\n{question}\n\n[설명]")
])

# 지원사업 추천 프롬프트
recommend_prompt = ChatPromptTemplate.from_messages([
    ("system", """
당신은 예비·초기 창업자에게 가장 적합한 '지원사업을 추천하는 전문가 AI'입니다.

[목표]
사용자의 조건(나이, 지역, 업종, 창업 단계 등)을 기준으로
'실질적인 도움이 되는 사업(자금·공간·R&D·시제품·교육)'을 우선적으로 추천합니다.

[추천 우선순위]
1. 현금성 지원(사업화 자금, 시제품 제작비, R&D)
2. 입주 공간, 장비 지원
3. 엑셀러레이팅, 멘토링
4. 단순 교육/특강은 마지막 순위

[추천 규칙]
1. 반드시 announcement 문서만 사용
2. 사용자 조건과 '지역·연령·단계·업종'이 명확히 맞는 것만 추천
3. 최대 2개까지만 추천
4. 조건이 맞는 사업이 없으면 솔직하게 말하기
5. IT·서비스업이면 '기술·콘텐츠·플랫폼' 키워드 포함 사업 우선

[출력 형식]
■ 추천 사업명
■ 왜 이 사용자에게 적합한지
■ 지원 내용(자금/공간/교육 중 무엇인지 명확히)
■ 신청 대상 요약
■ 접수 기간
■ 주의사항

마지막 줄: [참고: 지원사업 공고]
"""),
    ("human", "[지원사업 문맥]\n{context}\n\n[사용자 조건]\n{question}\n\n위 형식에 맞춰 추천해 주세요.")
])

# Fallback 프롬프트
fallback_prompt = ChatPromptTemplate.from_template("""
질문: {question}

내부 문서에서 관련 정보를 찾지 못했습니다.
일반적인 지식을 바탕으로 답변해주세요.

답변:""")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 체인 생성
qt_chain = qt_prompt | llm | StrOutputParser()
multi_query_chain = multi_query_prompt | llm | StrOutputParser()
relevance_chain = relevance_check_prompt | llm | StrOutputParser()
fallback_chain = fallback_prompt | llm | StrOutputParser()

# ========================================
# 헬퍼 함수
# ========================================

def choose_prompt(question: str):
    """질문 유형에 따라 적절한 프롬프트 선택"""
    recommend_keywords = ["추천", "맞는", "신청할 수 있는", "지원해주는", 
                         "사업 알려줘", "혜택", "지원금", "지원사업"]
    law_keywords = ["정의", "자격", "요건", "지원법", "법에서", "법상", "제도", "시행","규정"]
    
    if any(k in question for k in recommend_keywords):
        return recommend_prompt, "recommend_prompt"
    if any(k in question for k in law_keywords):
        return law_prompt, "law_prompt"
    return rag_prompt, "rag_prompt"

def format_docs_as_context(docs):
    """RAG 프롬프트에 넣기 좋은 컨텍스트로 변환 (출처 메타데이터 포함)"""
    if not docs:
        return ""
    parts = []
    for i, d in enumerate(docs, 1):
        if isinstance(d, Document):
            src = d.metadata.get("source", d.metadata.get("url", "unknown"))
            parts.append(f"[문서 {i}] (출처: {src})\n{d.page_content}")
    return "\n\n---\n\n".join(parts)

def search_documents_hybrid(queries: List[str], k_per_query=10) -> List[Tuple[Document, float]]:
    """하이브리드 리트리버로 멀티쿼리 검색"""
    all_docs_with_scores = []
    seen_hashes = set()
    
    if hybrid_retriever is None:
        # Fallback: Dense만 사용
        print("[검색] 하이브리드 리트리버 없음, Dense만 사용")
        for q in queries:
            try:
                docs = vectorstore.similarity_search_with_score(q, k=k_per_query)
                for doc, distance in docs:
                    doc_hash = hashlib.md5(doc.page_content[:500].encode()).hexdigest()
                    if doc_hash in seen_hashes:
                        continue
                    seen_hashes.add(doc_hash)
                    similarity = max(0.0, 1.0 - (distance / 2.0))
                    all_docs_with_scores.append((doc, similarity))
            except Exception as e:
                print(f"⚠ 검색 오류: {e}")
        return all_docs_with_scores
    
    # 하이브리드 검색
    print(f"[하이브리드 검색] {len(queries)}개 쿼리로 검색 중...")
    for q in queries:
        try:
            docs_with_scores = hybrid_retriever.invoke(q)   # Dense + BM25 하이브리드 검색을 수행
            
            for doc, score in docs_with_scores:
                doc_hash = hashlib.md5(doc.page_content[:500].encode()).hexdigest()
                if doc_hash in seen_hashes:
                    continue
                seen_hashes.add(doc_hash)
                all_docs_with_scores.append((doc, score))
        except Exception as e:
            print(f"⚠ 하이브리드 검색 오류: {e}")
    
    # 점수 기준 정렬
    all_docs_with_scores.sort(key=lambda x: x[1], reverse=True)
    return all_docs_with_scores

def check_relevance(question, docs_with_scores):
    """LLM에게 상위 N개 문서로 관련성 물어보기 -> True/False 반환"""
    # docs_with_scores는 (doc, sim)
    top_docs = docs_with_scores[:5]
    if not top_docs:
        return False
    # Document 객체에서 직접 접근
    docs_text = "\n\n---\n\n".join(
        f"[문서 {i+1}] (출처: {getattr(doc.metadata,'get',lambda k, d=None: 'unknown')('source','unknown')})\n{getattr(doc,'page_content',str(doc))[:600]}"
        for i, (doc, _) in enumerate(top_docs)
    )
    try:
        res = relevance_chain.invoke({"question": question, "documents": docs_text})
        return "관련있음" in res
    except Exception as e:
        print(f"⚠ 관련성 검증 오류: {e}")
        return False

def web_search(query: str, k=3):
    """Tavily API 기반 웹검색
    외부 소스만 Document로 변환 필요"""
    try:
        retriever = TavilySearchAPIRetriever(k=k)
        results = retriever.invoke(query) 

        # Tavily 결과를 Document로 정규화
        docs = []
        for r in results:
            if isinstance(r, Document):
                docs.append(r)
            elif isinstance(r, dict):
                content = r.get("content") or r.get("snippet") or r.get("title") or str(r)
                docs.append(Document(
                    page_content=content,
                    metadata={"source": "web", "url": r.get("url", "unknown")}
                ))
            else:
                docs.append(Document(
                    page_content=str(r),
                    metadata={"source": "web"}
                ))
        return docs
        
    except Exception as e:
        raise RuntimeError(f"Tavily 웹검색 오류: {e}")

# -----------------------
# RAG 응답 생성 함수
# -----------------------
def rag_answer_from_docs(question: str, documents):
    """문서 리스트(Document 또는 (doc,score) 혼합)을 받아 RAG 응답 생성
    이미 Document 형식이므로 tuple만 풀어주면 됨"""
    # tuple 형식이면 Document만 추출
    docs = []
    for item in documents:
        if isinstance(item, tuple):
            docs.append(item[0])  # (doc, score) → doc
        else:
            docs.append(item)     # 이미 Document
    
    context = format_docs_as_context(docs)
    if not context.strip():
        print("⚠ context 비어있음 -> fallback LLM로 이동")
        return fallback_chain.invoke({"question": question})

    prompt, pname = choose_prompt(question)
    print(f"[프롬프트 사용] {pname} (문서 기반)")
    
    try:
        answer = (prompt | llm | StrOutputParser()).invoke({
            "context": context,
            "question": question
        })
        return answer
    except Exception as e:
        print(f"⚠ RAG 생성 오류: {e}")
        return fallback_chain.invoke({"question": question})
    
# ========================================
# 메인 RAG 함수
# ========================================
# 멀티레벨 캐시 초기화
if cache_db_ok:
    multi_level_cache = MultiLevelCache(cache_vectorstore=cache_vectorstore)
    print("✅ 멀티레벨 캐시 초기화 완료\n")
else:
    multi_level_cache = None
    print("⚠ 캐시 DB 없음 - 캐시 비활성화\n")

def multi_query_rag_with_cache(question: str, top_k=10):
    """
    전체 흐름:
      1) 쿼리 트랜스폼 (QT)
      2) 멀티쿼리 생성 (MQ)
      3) 벡터검색 (멀티쿼리)
      4) 유사도 필터링
        - 문서 있음 -> LLM 관련성 검증
        - 문서 없음 / 관련 없음 -> 웹검색 또는 Fallback (단일 분기)
    """

  # 실제 RAG 로직 (캐시 미스 시 호출됨)
    def execute_rag(question):
        # 1) Query Transform
        try:
            qt_query = qt_chain.invoke({"question": question})
            print(f"[1단계] QT 완료: {qt_query}")
        except Exception as e:
            print(f"⚠ QT 실패: {e}")
            qt_query = question

        # 2) Multi Query
        try:
            mq_text = multi_query_chain.invoke({"question": qt_query})
            queries = [line.strip() for line in mq_text.splitlines() if line.strip()]
            print(f"[2단계] 멀티쿼리 생성: {len(queries)}개")
            for i, q in enumerate(queries, 1):
                print(f"  {i}. {q}")
        except Exception as e:
            print(f"⚠ 멀티쿼리 실패: {e}")
            queries = [qt_query]

        # 3) 하이브리드 검색
        print(f"[3단계] 하이브리드 검색 시작...")
        all_docs_with_scores = search_documents_hybrid(queries, k_per_query=10)
        print(f"[3단계] 검색 완료: {len(all_docs_with_scores)}개 문서")

        # 4) 상위 문서 필터링
        top_docs = all_docs_with_scores[:top_k]

        if top_docs:
            print(f"[4단계] 상위 {len(top_docs)}개 문서 확보")
            # 관련성 검증
            is_relevant = check_relevance(question, top_docs)
            
            if is_relevant:
                print("✅ [5단계] 내부 문서가 관련있음 → 내부 RAG 실행")
                return rag_answer_from_docs(question, top_docs)
            else:
                print("⚠ [5단계] 내부 문서 관련없음 → 웹검색 시도")
        else:
            print("⚠ [4단계] 내부 문서 없음 → 웹검색 시도")

        # 5) 웹 검색
        try:
            print("[6단계] 웹 검색 중...")
            web_docs = web_search(question)
            if web_docs:
                print(f"✅ [6단계] 웹 문서 {len(web_docs)}개 확보 → 웹 RAG 실행")
                return rag_answer_from_docs(question, web_docs)
            else:
                print("⚠ [6단계] 웹 검색 결과 없음 → Fallback")
                return fallback_chain.invoke({"question": question})
        except Exception as e:
            print(f"⚠ 웹검색 실패: {e} → Fallback")
            return fallback_chain.invoke({"question": question})

    # 캐시 사용
    if multi_level_cache:
        return multi_level_cache.get(question, execute_rag)
    else:
        print("⚠ 캐시 없음 → 직접 RAG 실행")
        return execute_rag(question)
# ========================================
# 테스트 실행
# ========================================

if __name__ == "__main__":
    test_cases = [
        "서울에서 AI 챗봇 창업을 하려고 하는데 받을 수 있는 지원사업 있나요?",
        "서울에서 AI 챗봇 창업을 하려고 하는데 받을 수 있는 지원사업 있나요?",
        #"헤어악세사리 사업했는데 판매가 매우 저조해. 어떻게 하면 될까?",
        "서울에 있는 동물병원 알려주세요",
    ]
    
    for i, q in enumerate(test_cases, 1):
        print("\n" + "-"*40)
        print(f"테스트 {i}/{len(test_cases)}")
        print("-"*40)
        print(f"질문: {q}")
        
        try:
            ans = multi_query_rag_with_cache(q)
            
            print("\n" + "-"*40)
            print("최종 답변")
            print("-"*40)
            print(ans)
            print("\n")
        except Exception as e:
            print(f" 오류 발생: {e}")
            import traceback
            traceback.print_exc()
    
    if multi_level_cache:
        multi_level_cache.stats()
    
    print("\n 테스트 완료!")

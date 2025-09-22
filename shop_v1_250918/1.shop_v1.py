# pip install pymysql # mysql을 접속할 수 있는 라이브러리
# pip install dotenv  # 환경변수 .env를 로드할수 있는 라이브러리
import pymysql
from dotenv import load_dotenv
import os
# .env 로드 # .env 파일 불러오기 → 보안 때문에 DB 정보는 코드에 직접 쓰지 않고 환경변수로 관리
load_dotenv()

# 1. DB 연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),        # DB 서버 주소 (.env에서 가져옴)
    user = os.getenv('DB_USER'),        # DB 사용자 이름
    password = os.getenv('DB_PASSWORD'), # DB 비밀번호
    database=os.getenv('DB_NAME')       # 접속할 데이터베이스 이름
)
print('접속성공')

# 2. 각 테이블별 
    # C - insert 고객 추가
    # R - select 전체 고객 조회
    # U - update 고객 이름 수정
    # D - delete 고객 삭제

# c 고객 - customer   # 고객 테이블에 새로운 고객 추가하는 함수
def create_customer(name):
    # SQL 구문: customer 테이블에 새로운 데이터 삽입
    # id(auto_increment)는 null로 두고, 이름만 삽입
    sql = 'insert into customer values(null,%s)'    # sql 문자열로 삽입 쿼리 준비
    cur = conn.cursor()         # conn 은 위에서 만든 DB연결 정보.커서(cursor) 생성: SQL 실행/결과 조회를 담당하는 객체  # conn 은 데이터베이스 연결 객체, .cursor() 매서드를 호출해서 커서 객체 생성
    cur.execute(sql, name)      # SQL 실행 (name을 매개변수로 바인딩) # SQL 실행 (name은 %s에 바인딩됨)
    conn.commit()               # DB에 변경사항 저장
    print('고객추가 완료')

# R - 고객 전체 조회
def readAll_customers(isDict = False):
    sql = 'select * from customer'     # customer 테이블의 모든 데이터 조회
    
    if isDict:           # DictCursor 사용: 각 행을 딕셔너리(컬럼명:값)으로 반환받음
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)            #SQL 실행
        for c in cur.fetchall():    # fetchall(): 모든 결과(행)를 리스트로 가져옴           
            print(f"{c['customer_id']}  {c['name']}") # 딕셔너리 접근: 컬럼명을 키로 사용
    else:               # 기본 튜플 형식으로 조회
        cur = conn.cursor() # 기본 커서: 튜플(인덱스) 형태로 결과 반환
        cur.execute(sql)
        for c in cur.fetchall():            
            print(f'{c[0]}  {c[1]}')  # 튜플 접근: 인덱스 0→customer_id, 1→name
    print('조회완료')    

# U - 고객 이름 수정    
def update_customer(customer_id, name):
    sql = '''
        update customer 
            set name = %s
        where customer_id = %s
    '''

    with conn.cursor() as cur:      # with 구문으로 커서 생성 → 블록 끝나면 커서 자동 close 됨
           # execute의 파라미터 순서는 SQL문의 %s 순서와 같아야 함
        # 여기서는 (name, customer_id)가 맞음 (첫 %s → name, 두번째 %s → customer_id)
            cur.execute(sql, (name, customer_id))  
    conn.commit()               # 변경사항 DB에 반영

# 삭제
def delete_customer(customer_id):
    sql = 'delete from customer where customer_id=%s'
    with conn.cursor() as cur:
        cur.execute(sql,customer_id)
    conn.commit()
    print(f'삭제되었습니다. {customer_id}')

# 테스트용
create_customer('abc')
readAll_customers()
update_customer(1,'abc')
delete_customer(1)

# 3. 메소드
    # 회원가입
    # 상품정보를 출력
    # 상품구입
    # 상품정보 입력
    # 대시보드: 고객별 상품별 구매횟수, 평균구매액
# 4. 기능구현과 테스트가 되면 streamlit으로 UI 구성 - 템플릿 화면을 보고 유사한 형태로 구현

conn.close() # 연결해제

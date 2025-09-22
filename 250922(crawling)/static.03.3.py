# shop_base2_tbl
# mysql에서 shop_base_tbl의 구조만 복사

# 1페이지 ~ 46페이지 크롤링
# 데이터 꺼내서 DB에 저장
# 새 데이터면 INSERT
# 이미 있으면 UPDATE (가게 상태, 주소, 전화번호 최신화)
# 모든 작업이 끝날 때마다 commit

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database='shopinfo'
    )

import crawlingcoffe
# 터미널에서 pip install tqdm
import tqdm                                 # tqdm 진행상황 표시를 위한 라이브러리
for page_num in tqdm.tqdm(range(1,47)):     # 47은 페이지 수
    datas = crawlingcoffe.get_data(page_num) # 크롤링한 데이터 리스트
    with get_connection() as conn:          # DB 연결을 자동으로 열고 닫음
        with conn.cursor() as cur:          # SQL 실행용 커서 생성
            for data in datas:
                try:
                    sql= 'insert into shop_base2_tbl value(%s,%s,%s,%s,%s)'
                    cur.execute(sql,(data[0],data[1],data[2],data[3],data[4]))
                except pymysql.err.IntegrityError:                                # update 새로운 데이터를 최신 값으로 덮어씀
                    sql = '''update shop_base2_tbl      
                            set shop_state=%s,shop_addr=%s, shop_phone_number=%s
                            where shop_area=%s and shop_name= %s'''
                    cur.execute(sql,((data[2],data[3],data[4],data[0],data[1])))
                    conn.commit()           # DB에 실제로 반영
                else:
                    conn.commit()


# database 접속
# insert 쿼리문을 이용해서 수집한 데이터를 DB에 저장

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
with get_connection() as conn:                     # DB 연결을 열고, 블록을 벗어나면 자동으로 닫힙니다
    with conn.cursor() as cur:                     # DB 명령을 실행할 커서를 만듭니다. 이 블록을 나가면 커서가 닫힘\
                                                   # null은 (보통) 자동증가되는 id 필드용이고, %s는 파라미터 자리표시자
        sql = '''                                  
            insert into shop_base_tbl
	            values(null,%s,%s,%s,%s,%s)
            '''
        # cur.execute(sql,( , , , ,  )  )           INSERT 쿼리를 준비하고 여러 행을 executemany()로 삽입
        cur.executemany(sql,crawlingcoffe.get_data())  # row를 구성하는 튜플들의 리스트
    conn.commit()                                       # commit()으로 확정(영구저장)
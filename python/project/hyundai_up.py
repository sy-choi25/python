# 크롤링한 데이터 sql에 저장하는 코드
import pymysql 
from dotenv import load_dotenv
import os

def hyundai_db(h_faq):
    if not h_faq:
        print("저장할 데이터가 없습니다.")
        return
    
load_dotenv()
args = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': 'sknfirst'
}

try:
    conn = pymysql.connect(**args)
    cursor = conn.cursor()
    print(f"✅ MySQL '{args['database']}' DB에 성공적으로 연결되었습니다!")
   
    sql = """
    CREATE TABLE IF NOT EXISTS faq (
        faq_id INT AUTO_INCREMENT PRIMARY KEY,         
        faq_major_category VARCHAR(100),
        faq_sub_category VARCHAR(100),
        faq_question TEXT,
        faq_answer TEXT
    )
    """    
    cursor.executemany(sql,h_faq)
    conn.commit()
    print(f"DB 저장 완료: {cursor.rowcount}개의 행이 처리되었습니다.")

    #sql = 'insert into faq (category, question, answer) values (%s, %s, %s)'
    # for data in result:
    #     cursor.execute(sql, (data[0], data[1], data[2]))
    #     print(data[2], data[5], data[1], data[3])
    # conn.commit()

except pymysql.MySQLError as err:
    print(f"MySQL 오류: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("🔌 MySQL 연결이 종료되었습니다.")


hyundai_db(h_faq)
h_faq= 
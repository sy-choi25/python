# pip install pymysql
import pymysql
# 1. DB 연결
conn = pymysql.connect(
    host = '127.0.0.1',    # 워크벤치 초기화면에서 host name 복붙
    user = 'root',
    password= 'root1234',
    database = 'shopdb'
)
print('접속성공')
conn.close() # 연결해제

# 2. 각 테이블별
    # C - insert
    # R - select
    # U - update
    # D - delete
# 3. 메소드
    # 회원가입
    # 상품정보를 출력
    # 상품구입
    # 상품정보 입력
    # 대시보드: 고객별 상품별 구매횟수, 평균구매액
# 4. 기능구현과 테스트가 되면 streamlit으로 UI 구성 - 템플릿 화면을 보고 유사한 형태로 구현

import requests
# 데이터를 요청할 주소
url= 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gugun' : '',
    'store' : ''
}
response = requests.post(url,data=from_data)

# 터미널에서 pip install beautifulsoup4실행
from bs4 import BeautifulSoup          #Beautifulsoup은 할리스 페이스 소스에서 보이는 양을 객체로 만들어서 가독성 있게 만들어줌
# response에 있는 문자열로 된 데이터를 Beautifulsoup 객체로 변환
soup = BeautifulSoup(response.text,'html.parser')

# 원하는 정보를 추출  할리스 웹페이지 f12에서 마우스표시로 정보를 클릭하면 보이는 소스코드에 tbody부분 copy> copy selector
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'  # 주소가 길어서 변수 선언
# tbody가 하나인 경우 soiup.select('tbody > tr')도 가능, 여러개의 경우 가장 먼저 만나는 tbody만 출력
store_rows = (soup.select(str_table_rows))

# 예시로 1번만 가져와보기
first_store = store_rows[0]                    # 1번 페이지 1번인 부산 남구의 정보를 가져올 수 있음
print(first_store.select('td')[0].text.strip())    # 부산 남구의 td 하나씩 출력  # 지역
print(first_store.select('td')[1].text.strip())    # 매장명
print(first_store.select('td')[2].text.strip())    # 현황
print(first_store.select('td')[3].text.strip())    # 주소
print(first_store.select('td')[5].text.strip())    # 전화번호

# 1페이지의 전체 가져오기. 반복문 사용
for row in store_rows:
    print(row.select('td')[0].text.strip())    
    print(row.select('td')[1].text.strip())    
    print(row.select('td')[2].text.strip())    
    print(row.select('td')[3].text.strip())   
    print(row.select('td')[5].text.strip()) 
    print('*'* 100)

# 몇번인지 인덱스랑 같이 추출
# for idx,row in enumerate(store_rows):
#     print(idx+1)
#     print(row.select('td')[0].text.strip())    
#     print(row.select('td')[1].text.strip())    
#     print(row.select('td')[2].text.strip())    
#     print(row.select('td')[3].text.strip())   
#     print(row.select('td')[5].text.strip()) 
#     print('*'* 100)



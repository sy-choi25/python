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
print(response.text[:500])      # 소스의 전체코드가 response.text가 들어있어서 최대 500으로 제한

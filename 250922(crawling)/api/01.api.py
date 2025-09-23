from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()


# .env에 있는 값
# PUBLIC_ENCODE_KEY='U5i63xpIWM48raIRQBYpUXbA%2FwKd0iO6n%2Fn1%2BJISyoEW1gWcEiz2No2fHPeid5TZoQN0HV85WyGv6LPwaQ8n4w%3D%3D'
# PUBLIC_DECODE_KEY='U5i63xpIWM48raIRQBYpUXbA/wKd0iO6n/n1+JISyoEW1gWcEiz2No2fHPeid5TZoQN0HV85WyGv6LPwaQ8n4w=='

# P_KEY = os.getenv('PUBLIC_ENCODE_KEY')
P_KEY = 'U5i63xpIWM48raIRQBYpUXbA%2FwKd0iO6n%2Fn1%2BJISyoEW1gWcEiz2No2fHPeid5TZoQN0HV85WyGv6LPwaQ8n4w%3D%3D'
# print(f'P_KEY : {P_KEY[-10:]}')
# 데이터를 요청 할 주소
# 디코딩/ 인코딩 키 구분해서 넣기
url = f'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?page=1&perPage=10&serviceKey={P_KEY}'      # getAPTLttotPblancDetail 이 부분 값을 내가 보고 싶은 키랑 변경하면 다른 정보도 불러올 수 있음
# url = f'http://apis.data.go.kr/B553881/newRegistInfoService/newRegistInfoService?serviceKey={P_KEY}&registYy=2017&registMt=09&vhctyAsortCode=1&registGrcCode=10&useFuelCode=2&cnmCode=&prposSeNm=1&sexdstn=남자&agrde=2&dsplvlCode=4&hmmdImpSeNm=국산&prye=2016'
# print(f'url={url}')
# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
# from_data = {
#     'serviceKey' : P_KEY,
#     'page':1,
#     'perPage':10     
# }
response = requests.get(url)
# print(response.text)
data_dict = response.json()
print(data_dict.keys())
import json
json_print = json.dumps(data_dict,indent=4,ensure_ascii=False)
print(json_print)
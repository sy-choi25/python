
# pip install selenium webdriver-manager
from selenium import webdriver                  # selenium: 브라우저 자동화를 위한 핵심 라이브러리
from selenium.webdriver.chrome.service import Service           # webdriver_manager: 크롬 드라이버를 자동으로 설치/업데이트 해줌 (매번 수동 다운로드 필요 없음)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By                     # By: HTML 요소를 찾을 때 사용하는 선택자 (id, class, xpath 등)
from selenium.webdriver.common.keys import Keys # 엔터 키 등을 입력하기 위해서      # Keys: 키보드 입력(Enter, Tab, ESC 등)을 시뮬레이션할 때 사용

import time

# 웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.google.com/')                       # 브라우저에서 구글 페이지 열기
print('브라우져가 성공적으로 열렸습니다.')
# driver.quit()
# 검색창 요소 찾기(id 가 'ipt_keyword_recruit'인 input 태그를 찾음)
search_input = driver.find_element(By.CLASS_NAME,"gLFyf")           # HTML에서 원하는 요소를 찾음
# 검색창에 파이썬 입력
search_input.send_keys('파이썬')
time.sleep(3)
# enter 키 누르기
 # 대략 3초 정도 페이지 로드 될 때까지 기다림
search_input.send_keys(Keys.ENTER)               # 실제 키보드에서 Enter 누르는 것처럼 동작.
time.sleep(5)
driver.quit()
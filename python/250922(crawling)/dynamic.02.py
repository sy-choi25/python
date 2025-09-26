
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://auto.danawa.com/auto/?Work=record'
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
driver.maximize_window() # 전체 화면으로 실행
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
WebDriverWait(driver,10).until(
    EC.presnece_of_element_located((By.CLASS_NAME, 'recordSection'))
)
driver.find_element(By.ID,'selMonth')
# 객체로 만든다
select_year = Select(year_select)
time.sleep(5)
select_year.select_by_value('2024')

month_select = drive.find.elemenr(By.ID,'selDay')
# 객체로 만든다
select_month = Select(month_select)
for i in range(1,13):
    select_month.select_by_value('01')

# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://auto.danawa.com/auto/?Work=record'
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
driver.maximize_window() # 전체 화면으로 실행
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
WebDriverWait(driver,10).until(   #최대 10초간 기다리겠다. until(조건) 조건이 만족될 때까지 기다린다
    EC.presnece_of_element_located((By.CLASS_NAME, 'recordSection'))
    )                               # 즉, "driver 안에서 CLASS_NAME이 'recordSection'인 요소가 나타날 때까지 최대 10초간 기다려라"
driver.find_element(By.ID,'selMonth')       # HTML 태그 중 id="selMonth"인 요소 찾기
# 객체로 만든다
select_year = Select(year_select)
select_year.select_by_value('2024')

time.sleep(1)

month_select = driver.find_element(By.ID,'selDay')
# 객체로 만든다
select_month = Select(month_select)
for i in range(1,13):
    select_month.select_by_value(f'{i:02d}')
    time.sleep(1)

time.sleep(10)
driver.quit()


# 전체 구조 요약
    # 크롬 드라이버 실행
    # 사이트 접속
    # 특정 요소 나타날 때까지 대기
    # 연도 선택 (드롭다운 제어)
    # 월 선택 (for문으로 반복)
    # 브라우저 종료
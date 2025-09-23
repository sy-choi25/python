from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# URL 설정
url = 'https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58'
# 웹 드라이버 설치 및 최신버전 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get(url)
driver.maximize_window()
time.sleep(10)

select = Select(driver.find_element(By.ID, 'sFormId'))
select.select_by_value('5498')
time.sleep(0.5)

form_btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]/div/button')
driver.execute_script('arguments[0].click()', form_btn)
time.sleep(1.5)

# 기간 선택
select = Select(driver.find_element(By.ID, 'sStart'))
select.select_by_value('202401')
time.sleep(0.5)
select = Select(driver.find_element(By.ID, 'sEnd'))
select.select_by_value('202401')
time.sleep(0.5)

# 조회 버튼
# //*[@id="main"]/div/div[2]/div[2]/div[3]/div/div[1]/div/div/div/button
btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[3]/div/div[1]/div/div/div/button')
driver.execute_script("arguments[0].click()", btn)
time.sleep(1.5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
str_table_rows = '#sheet01-table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.GMPageOne > table > tbody > tr'
month_rows = soup.select(str_table_rows)

# print(month_rows, '\n')
# print(month_rows.select('td')[1])

month_lists = []
x
for i in month_rows :
    temp_list = []

    try :
        i_list = i.select('td')
        for j in i_list :
            # print(j.text.strip())
            temp_list.append(j.text.strip())
    except Exception as e:
        print(e)
    
    month_lists.append(temp_list)

for i in month_lists :
    print(i)

# for idx, i in enumerate(month_rows) :
#     for j in range(1, 18) :


time.sleep(10)
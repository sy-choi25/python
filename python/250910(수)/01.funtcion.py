# import random
# random.randint(1,5) # 랜덤하게 1~4까지의 숫자를 뽑는다
# # 이 숫자를 알고 싶다면 print 나 result로 받는다
# # print(random.randint(1,5))  / 혹은 result = random.randint(1,5)
# # print 는 반환하지 않음. 반환되지 않으면 None로 표현됨
# print(random.randint(1,5))

# 함수정의 def 키워드 사용
# 매개변수(Parameter) : 함수가 전달받는 값
# 인자(Agument)       : 함수를 호출할 때 전달하는 값
# 반환값(Return Value): 함수가 작업을 마치고 호출한 곳으로 돌려주는 값 / return 키워드 사용

# 함수의 구성요소
# 기본식
def myCalc(num1, num2):
    result = num1+num2
    return result

myCalc(1,2)


def myCalc(num1, num2):
    ''' 
    두 개의 값을 받아 더하는 기능
    num1은 숫자
    num2는 숫자
    '''
    result = num1+num2
    return result

myCalc(1,2)

# 함수 케이스
# 1. 매개변수와 반환값이 없는 함수
def say_hello():
    print('안녕하세요')

say_hello()   # 호출할 때 -> 안녕하세요 가 프린트 됨
print(say_hello()) # 반환값이 없기 떄문에 None 값이 나오는 것이 맞음

# 2. 매개변수가 있고 반환값이 없는 함수
def say_hello_name(name):
    print(f'{name}님 안녕하세요')

say_hello_name("소영")
# -> 소영님 안녕하세요

# 3. 매개변수가 없고 반환값이 있는 함수
import datetime

def get_current_time():
    return datetime.datetime.now()

print(get_current_time())
#------------------------------



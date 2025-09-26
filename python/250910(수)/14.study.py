# 매개변수 o, 반환값 o
# 1)
def multiply(a, b):
    result = a* b
    return result

print( multiply(3, 5))

# 2)
# 문제: 두 수를 입력 받아 더한 값을 반환하는 함수 add_numbers를 만들어보세요.

def add_number (a,b):
    return a + b

print(add_number(7,5))



# 매개변수 o, 반환값 x
# 1)
# 문제: 이름을 입력 받아서 "OO님 안녕하세요"를 출력만 하는 함수 say_hello를 만들어보세요.

def say_hello(name):
    print(f'{name}님 안녕하세요')

say_hello('소영')
#2)
# 문제: 이름과 나이를 입력 받아 "OO님, 나이는 XX살입니다"를 출력만 하는 함수 introduce를 만들어보세요.

def introduce(name, age):
    print(f'{name}님, 나이는 {age} 입니다')

print(introduce("소영","25"))


#매개변수 x, 반환값 o
#1)
# 문제: 어떤 상수 값을 이용해서 "파이의 값: 3.14"를 반환하는 함수 
# get_pi를 만들어보세요.

def get_pi():
    pi = 3.14
    return pi

print(get_pi())

# 2)
# 문제: 오늘 날짜를 문자열로 반환하는 함수 get_today를 만들어보세요. (예: "2025-09-10")
#  첫번쨰방법
def get_today():
    today = "2025-09-10"
    return today

print(get_today())

# 두번째방법

import datetime

def get_today():
    today = datetime.date.today()
    return str(today)

print(get_today())


#매개변수 x, 반환값 x
# 1)
# 문제: "파이썬 공부 재미있다!"를 출력만 하는 함수 study_python을 만들어보세요.

def study_python():
    print("파이썬 공부 너무 재밌다")

study_python()

# 2)
# 문제: "파이썬 공부 열심히 합시다!"를 출력만 하는 함수 encourage를 만들어보세요.

def encourage():
    print("파이썬 공부를 열심히 합시다")

encourage()
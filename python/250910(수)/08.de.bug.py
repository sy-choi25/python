# 변수명이 다를 떄 치환가능

def say_hello(A):
    return f'{A} 님 반가워요'

name = '홍길동'
result = say_hello(name)        # A와 name의 변수명은 다르지만 이 과정에서 동일한 변수로 치환
print(result)

# -> 홍길동님 반가워요



#함수 double_number를 만들어서,
#숫자를 하나 받아서 2배 한 값을 반환하세요.

#def double_number(x):
#실행 예시:

#num = 5
#result = double_number(num)
#print(result)   # 출력: 10'''


def double_number(x):
    return x*2

num = 5
result = double_number(num)
print(result)
# ===============================
# 📘 파이썬 복습 문제 (자료형 ~ 문자열 ~ 숫자 연산)
# ===============================

# 1. 자료형 기초 --------------------
# 1) 변수 a = 10, b = -3 을 만들고 각각의 자료형을 출력하세요.

a = 10
b = -3

print(type(a))
print(type(b))

# 2) 변수 pi = 3.14, is_ready = False 의 자료형을 출력하세요.

pi = 3.14
is_ready = False

print(type(pi))
print(type(is_ready))

# 2. 문자열 조작 --------------------
# 1) first_name = "길동", last_name = "홍" 을 이용해 "홍길동"을 출력하세요.

first_name = "길동"
last_name = "홍" 
print(last_name+first_name)

# 2) "홍길동" 문자열의 길이를 구하세요.

print(len("홍길동"))

# 3) "홍길동"에서 "길"만 출력하세요.

list_a = "홍길동"
print(list_a[1])

# 4) "홍길동"에서 마지막 글자를 출력하세요.

print(list_a[-1])

# 5) "안녕"을 3번 반복해서 출력하세요.

print("안녕"*3)

# 3. 문자열 줄바꿈 --------------------
# 1) "동해물과\n백두산이" 를 출력하면 어떤 모양이 될까요?

print("동해물과\n백두산이")

# 2) '''동해물과\n백두산이''' 처럼 삼중 따옴표로 출력하면 어떻게 될까요?

print('''동해물과\n백두산이''')

# 4. 문자열 슬라이싱 --------------------
# 주어진 문자열 message = "python is powerfull" 을 가지고:
message = "python is powerfull"

# 1) 문자열 길이를 구하세요.
print(len(message))
# 2) 첫 번째 문자만 출력하세요.
print(message[0])
# 3) "python"만 출력하세요.
print(message[0:6])
# 4) "is powerfull"만 출력하세요.
print(message[6:])
# 5) 마지막 글자를 출력하세요.
print(message[-1])

# 5. 포맷스트링 --------------------
# 아래 변수로 "8월 1005동 1001호 관리비는 250000입니다" 라는 문장을 만드세요.
month = 8
dong = 1005
ho = 1001
apt_price = 250000

# 👉 방법 2가지
# 1) str() 변환 + + 연산자
report = str(month) +"월 "+str(dong) +"동 "+str(ho)+"호 관리비는 "+str(apt_price)+"입니다"
print(report)
# 2) f-string
print(f'{month}월 {dong}동 {ho}호 관리비는 {apt_price:,}입니다')

# 6. 숫자 연산 --------------------
num1 = 10
num2 = 25

# 1) num2 / num1 값을 출력하세요.
print(num2/num1)
# 2) num2 // num1 값을 출력하세요.
print(num2//num1)
# 3) num2 % num1 값을 출력하세요.
print(num2%num1)
num1 = 5
# 4) num1 ** 3 (세제곱) 결과를 출력하세요.
num1 = 10
num2 = 25
print(num1**3)

# 5) 복합 대입연산자 (+=)를 사용해서 price 값을 12로 만드세요.

price = 10
price += 2
print(price)
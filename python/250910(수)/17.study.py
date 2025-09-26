# ===============================
# 파이썬 연습문제 예시 (VS Code에서 바로 실행 가능)
# ===============================

# -------------------------------
# 1️⃣ 자료형 & 연산
# -------------------------------

# [개념확인] 숫자 a=10, b=3을 만들고 더하기, 빼기, 나누기, 나머지 출력
a = 10
b = 3
print(a+b)
print(a-b)
print(a/b)
print(a%b)


# TODO: 아래에 연산 결과 출력
# 예: print(a+b)

# [응용(초급)] 변수 x=7, y=2.5를 만들어서 곱하기, 나누기 결과를 소수점 둘째자리까지 출력
x = 7
y = 2.5

# TODO: print(f"{x*y:.2f}") 같은 방식으로 출력
print(x*7)
result= x/y
print(f"결과: {result:.2f}")
# [중급] 사용자에게 두 수를 입력받아 합과 평균을 출력
num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))

# TODO: 합과 평균 출력
# 예: print(f"합: {합}, 평균: {평균}")

print(f"합: {num1+num2}, 평균: {(num1+num2)/2}")
# -------------------------------
# 2️⃣ 문자열
# -------------------------------

# [개념확인] 문자열 name="홍길동"의 길이와 첫 글자, 마지막 글자 출력
name = "홍길동"
print(len(name))
print(name[0])
print(name[-1])
# TODO: print(len(name)), print(name[0]), print(name[-1])

# [응용(초급)] "안녕하세요"를 5번 반복하고 출력
greeting = "안녕하세요"
print(greeting*5)
# TODO: print(greeting*5)

# [중급] 사용자로부터 이름과 나이를 입력받아 "홍길동님은 20세입니다." 출력
user_name = input("이름 입력: ")
user_age = int(input("나이 입력: "))

print(f'{user_name}님은 {user_age}세 입니다')

# TODO: print(f"{user_name}님은 {user_age}세입니다.")


# -------------------------------
# 3️⃣ 리스트 & 반복문
# -------------------------------

# [개념확인] 리스트 numbers=[1,2,3,4,5]에서 3번째 요소 출력
numbers = [1,2,3,4,5]

print(numbers[2])

# [응용(초급)] numbers 리스트에서 짝수만 찾아 출력
# 힌트: for 문과 if 사용

import random
numbers = random.sample(range(1, 11), 5)
print(f'전체 숫자: {numbers}')

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print(f'짝수들의 집합: {even_numbers}, 갯수: {len(even_numbers)}')

# TODO: for i in numbers: ... append 짝수
print(even_numbers)

# [중급] 1~10 숫자를 리스트로 만들고, 홀수만 모아서 새로운 리스트에 저장 후 출력
numbers2 = list(range(1,11))

odd_numbers = []
for i in numbers2:
    if i % 2 > 0:
        odd_numbers.append(i)
print(f'홀수들의 집합{odd_numbers}, 갯수 {len(odd_numbers)}')

# TODO: for 문 사용
print(odd_numbers)


# -------------------------------
# 4️⃣ 함수 & 랜덤
# -------------------------------

# [개념확인] 두 숫자를 더하는 함수 add(a,b) 작성 후 5+3 출력
def add(a,b):
    # TODO: return 결과
    pass

def add(a,b):
    return a+b
print(add(5,3))

# [응용(초급)] 숫자를 하나 받아 2배로 반환하는 함수 double_number(num) 작성
def double_number(num):
    # TODO: return 결과
    pass


def double_number(unm):
    return unm*2

unm = int(input("숫자를 입력해주세요"))
print(double_number(unm))


# [중급] 0~10 사이의 랜덤 숫자 5개를 리스트에 저장하고 합을 출력
import random
rand_list = random.sample(range(11),5)


# TODO: 합 계산 및 출력
# 예: print(sum(rand_list))


# -------------------------------
# 5️⃣ 조건문 & 가위바위보
# -------------------------------

# [개념확인] 숫자 score = 85가 60 이상이면 합격, 아니면 불합격 출력
score = 85

if score >= 60 :
    print("합격")
else:
    print("불합격")
    
# TODO: if-else 사용

# [응용(초급)] 사용자로부터 점수를 입력받아 90:A, 80:B, 70:C, 60:D, 나머지:F 학점 출력
score2 = int(input("점수 입력: "))

# TODO: if-elif-else 사용

# [중급] 간단한 가위바위보 게임
# 1:가위 2:바위 3:보
import random
com_choice = random.randint(1,3)
human_choice = int(input("입력(1:가위 2:바위 3:보): "))

# TODO: 승패 판단 및 출력
# if com_choice==human_choice -> 비김
# elif (조건문) -> 이김
# else -> 짐

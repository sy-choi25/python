# for 반복문은 두 가지가 존재

# 1) 시퀀스를 순환하는 반복문
#리스트, 튜플, 문자열, 딕셔너리, 집합(set) 등 순서가 있는 자료를 하나씩 꺼내면서 반복
# 구조: 
for 변수 in 시퀀스:
    
# 예시
# 리스트 순환
fruits = ['사과','바나나','딸기']
for fruit in fruits:
    print(fruit)
# 문자열 순환
word = "hello"

for ch in word:
    print(ch)


# 2)범위 기반 반복문 (range() 사용)
# 숫자 범위를 지정하여 반복
# 구조
for 변수 in range(시작, 끝, 증가):
   
# 예시
for i in range(5):
    print(i)
# ==============================
# 1. 자료형과 연산자
# a = 10, b = 3 일 때, 나머지와 몫을 구해 각각 c, d에 저장하고 출력
a = 10
b = 3

c= 10//3
d= 10 % 3
print(f'몫: {c}')
print(f'나머지: {d}')

# ==============================
# 2. 리스트
# fruits = ["apple", "banana", "cherry"]에서 "banana" 제거 후 "orange" 추가 후 출력
fruits = ["apple", "banana", "cherry"]

del fruits[1]
fruits.append("orange")
print(fruits)

# ==============================
# 3. 튜플과 언패킹
# t = (1,2,3)에서 첫 번째 값은 a, 나머지는 b, c에 저장
t = (1,2,3)

a,b,c = t

# ==============================
# 4. 딕셔너리
# scores = {"영희":90, "철수":80}, "유리":70 추가, 철수 점수 85로 변경
scores = {"영희":90, "철수":80}

scores["유리"] = 70
scores["철수"] = 85

print(scores)

# ==============================
# 5. 조건문
# age = 20, 20 이상 "성인", 미만 "미성년"
age = 20

if age < 20:
    print("미성년")
else:
    print("성인")
     
# ==============================
# 6. 반복문
# numbers = [1,2,3,4,5], 각 수의 제곱 출력
numbers = [1,2,3,4,5]

for i in numbers:
    print(i**2)
# ==============================
# 7. 함수
# 두 수 합계를 반환하는 함수 작성, 3과 5로 테스트

def sum(a,b):
    return a+b
print(sum(3,5))
# ==============================
# 8. 클래스 기본
# Student 클래스: 이름, 나이 속성, info() 메서드 "이름:__, 나이:__" 출력
# 객체 생성 후 info() 호출
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'이름:{self.name}, 나이:{self.age} ')

s = Student("영희", 20)
s.info()
# ==============================
# 9. 클래스 상속
# Animal 클래스 sound() "...", Dog 재정의 "멍멍"
# 객체 생성 후 sound() 호출

class Animal():
    def sound(self):
        print("동물 소리")

class Dog(Animal):
    def sount(self):
        print("멍멍")

d = Dog()
d.sound()


# ==============================
# 10. Getter/Setter
# Product 클래스: price 음수 불가
# p = Product(100), p.price=-50, price 출력

class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value

p = Product(100)
p.price = -50
print(p.price)
    
# ==============================
# 11. 예외 처리
# 사용자 입력을 정수로 변환, 숫자가 아니면 "숫자만 입력하세요"
try:
    num = int(input('숫자를 입력하세요'))
except ValueError:
    print('숫자만 입력하세요')

# ==============================
# 14. 리스트/딕셔너리 고급
students = [{"name":"영희","score":90},{"name":"철수","score":80}]
# score만 추출해 합계 출력
scores = [] 
for s in students:      
    scores.append(s["score"]) 

print(scores)
print(sum(scores))


scores= [s["score"]for s in students]
# ==============================
# 15. 반복문 응용
# 1~100 사이 3의 배수만 리스트로 출력

three = []
for i in range(1,101):
   if i % 3 == 0:
       three.append(i)
print(three)

three = [i for i in range(1, 101) if i % 3== 0]
print(three)
# ==============================
# 16. 람다와 map/filter
# nums=[1,2,3,4,5], 각 수에 2 곱한 리스트 람다+map으로 출력

doubled = list(map(lamba x : x*2, nums ))
print(doubled)

# ==============================
# 17. 클래스 다형성
# Animal 클래스 method(), Dog, Cat에서 재정의
# 반복문으로 두 객체 method() 호출

class Animal():
    def method(self):
        print("동물 매서드")
class Dog(Animal):
    def method(self):
        print("강아지 메서드")
class Cat(Animal):
    def method(self):
        print("고양이 메서드")

for i in [Dog(),Cat()]:
    i.mothod()

# ==============================
# 19. 가변 매개변수
# def add(*nums): 여러 수 더하고 결과 출력, 
add(1,2,3,4)

def add(*nums):
    return sum(nums)

print(add(1,2,3,4)) 
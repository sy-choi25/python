# ===============================
# 1️⃣ 조건문 + 반복문
# ===============================
# 문제: 1~50 사이 숫자 중 3의 배수이거나 5의 배수인 숫자만 출력
# 단, 15의 배수는 "FizzBuzz"라고 출력

fif = []
for i in range(1,51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 or i % 5 == 0:
        print(i)
# ===============================
# 2️⃣ 리스트 / 딕셔너리
# ===============================
# 문제: 리스트 [12,7,5,64,14,10]에서 10 이상인 수만 뽑아
# 인덱스와 값으로 딕셔너리 생성

list_a = [12,7,5,64,14,10]
list_b = [i for i in list_a if i >=10]

dict_b = {idx: val for idx, val in enumerate(list_b)}

print(list_a)
print(list_b)


# 3️⃣ 함수 / *args / **kwargs
# ===============================
# 문제: 여러 숫자를 받아 짝수만 합계를 반환하는 함수 even_sum(*args) 작성
def even_sum(*args):
    total = 0
    for i in args:
        if i %2 == 0:
            total += i
    return total
# 문제: 키워드 인자를 받아 가장 큰 값 반환 함수 max_value(**kwargs) 작성
def max_valuse(**kaargs):
    return max(kwrgs.valuses())

# ===============================
# 4️⃣ 클래스 / 상속 / 다형성
# ===============================
# 문제: Shape 클래스 작성, area() 메서드 정의
# Circle, Rectangle 클래스 상속, 각각 면적 계산
# 반복문으로 객체 리스트 순회하며 area() 호출

class Shape():
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        pass

shapes = [Circle(5), Rectangle(4,6)]
for shape in shapes:
    shape.area()
   
# ===============================
# 5️⃣ property / setter / getter
# ===============================
# 문제: Student 클래스 작성, score 속성은 0~100 범위만 허용
# setter로 조건 검사, getter로 점수 반환
class Student():
    def __init__(self, score):
        self._score = score
        
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self,value):
        if 0 <= value <= 100:
            self._score = value
        else:
            print("점수는 0~100사이여아 합니다")

s1 = Student(85)

# ===============================
# 6️⃣ map / filter / lambda
# ===============================
# 문제: 리스트 [4,7,10,15,20]에서 5의 배수만 뽑아 3배로 변환
list_a = [4,7,10,15,20]

result = map(lambda i: i * 3, filter(lambda i: i % 5 == 0, list_a))

print(list(result))
# ===============================
# 7️⃣ 리스트 / 딕셔너리 컴프리헨션
# ===============================
# 문제: 1~10까지 제곱수가 짝수인 경우만 딕셔너리로 생성 {숫자: 제곱}'
dict_c = {i : i ** 2 for i in range(1,11) if (i**2)% 2 == 0}



# ===============================
# 8️⃣ 중첩 반복문 / 튜플 언패킹
# ===============================
# 문제: 2차원 리스트 [[1,2,3],[4,5,6],[7,8,9]] 각 행의 합을 출력

for a,b,c, in list_a:
    print(a+b+c)

# 문제: 리스트 [(1,2),(3,4),(5,6)]에서 각 튜플 요소를 변수에 언패킹 후 곱 출력

list_a = [(1,2),(3,4),(5,6)]
list_a[0][0],list[0][1],list_a[1],list_a[2] = tu1

for i in list_a

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):          # getter 역할
        return self._age

    @age.setter
    def age(self, value):   # setter 역할
        if value < 0:
            print("나이는 음수가 될 수 없습니다.")
        else:
            self._age = value


# 객체 생성
p = Person("철수", 20)

# getter 사용
print(p.age)       # 20

# setter 사용
p.age = 30         # value = 30
print(p.age)       # 30

# setter 조건 실패
p.age = -5         # value = -5 → 음수라서 저장 안 됨
print(p.age)       # 여전히 30
# =========================
# 1. 자료형 / 변수
# 문제: 변수 a, b에 각각 10, 20을 저장하고, 두 변수의 합을 출력
# =========================
a= 10
b= 20
print(a+b)
# =========================
# 2. 리스트 / 딕셔너리
# 문제: 리스트 [1,2,3,4,5]에서 짝수만 모아 새로운 리스트를 만들고 출력
# =========================
list_a = [1,2,3,4,5]
new = []
for i in list_a:
    i % 2 == 0
    new.append(i)
print(new)

# =========================
# 3. 조건문
# 문제: 사용자 입력 숫자가 0보다 크면 "양수", 0이면 "0", 음수면 "음수" 출력
# =========================
answer = int(input("숫자를 입력하세요"))
if answer > 0:
    print("양수")
elif answer == 0:
    print(0)
else:
    print("음수")
# =========================
# 4. 반복문
# 문제: 1~10까지 합을 구하고 출력
# =========================
list_b = []
for i in range(1,11):
    list_b.append(i)
print(sum(list_b))
# =========================
# 5. 함수
# 문제: 두 숫자를 매개변수로 받아 큰 수를 반환하는 함수 작성 후 테스트
# =========================
def sumi(a,b):
    print(max(a,b))

sumi(4,7)
# =========================
# 6. 클래스
# 문제: Book 클래스를 만들고, 제목(title), 저자(author) 속성을 초기화, 
# __str__ 메서드로 "제목: XXX, 저자: XXX" 형태로 출력. 객체 하나 만들어 출력

# =========================
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'제목: {self.title}, 저자: {self.author}' 

a = Book("햄릿", "세익스피어")
print(a)
# =========================
# 7. 상속
# 문제: Animal 클래스에 speak() 메서드 정의
# Dog 클래스는 Animal 상속, speak() 재정의해서 "멍멍" 출력
# Cat 클래스는 Animal 상속, speak() 재정의해서 "야옹" 출력
# 반복문으로 두 객체 speak() 호출
# =========================
class Animal():
    def speak(self):
        print("소리를 냅니다")

class Dog(Animal):
    def speak(self):
        print("멍멍")

class Cat(Animal):
    def speak(self):
        print("야옹")
d = Dog()
c = Cat()

ani =[d,c]
for i in ani:
    i.speak()


# =========================
# 8. 예외 처리
# 문제: 사용자 입력을 정수로 변환. 숫자가 아니면 "숫자만 입력하세요" 출력
# =========================

try:
    answer = int(input("숫자를 입력하세요"))
    print("입력한 숫자:",answer)
except ValueError:
    print("숫자만 입력하세요")


# =========================
# 10. 내장함수
# 문제: 리스트 [5,2,9,1,7]의 최대값, 최소값, 정렬된 리스트 출력
# =========================
list_a = [5, 2, 9, 1, 7]
print(max(list_a))
print(min(list_a))
print(sorted(list_a))

# =========================
# 11. map / filter / lambda
# 문제: 리스트 [1,2,3,4,5]에서 짝수만 추출하고 2배로 만들어 리스트로 출력
# =========================
list_a=[1,2,3,4,5]
pair = filter(lambda x: x%2 ==0, list_a)
double = map(lambda x: x * 2, pair)

result = list(double)
print(result)
# =========================
# 12. set / tuple
# 문제: 리스트 [1,2,3,2,1]에서 중복 제거하고 set과 tuple로 각각 출력
# =========================
list_a = [1,2,3,2,1]
# set으로 중복 제거
set_a = set(list_a)
print(set_a)           # {1, 2, 3}

# set을 tuple로 변환
tuple_a = tuple(set_a)
print(tuple_a) 
# =========================
# 13. 가변 매개변수
# 문제: *args로 여러 숫자를 받아 합계를 반환하는 함수 작성, 테스트
# =========================
list_a = ( 1, 3, 5)
def sum_mum(*args):
    return sum(args)

print(sum_mum(1,2,3))

# =========================
# 14. 기본 매개변수 / 키워드 가변 매개변수
# 문제: def info(name="무명", **kwargs) 사용
# 이름과 추가 정보(나이, 직업 등)를 출력
# =========================
def info(name="무명", **kwargs):
    print(name)
    for key,value in kwargs.item():
        print(f'{key}: {value}')

a= info("영수", 30, "선생님")
# =========================
# 15. 클래스 속성 / 인스턴스 속성 / property
# 문제: Product 클래스 작성, price는 음수 불가
# price 값을 설정, getter/setter 테스트
# =========================
class Product():
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value < 0 :
            print('가격은 음수가 될 수 없습니다')
        else:
            self.price = value
    
# =========================
# 18. 리스트 / 딕셔너리 컴프리헨션
# 문제: 1~10까지 제곱수를 딕셔너리 {숫자: 제곱}로 만들어 출력
# =========================
num = []
double = []
for i in range(1,11):
    num.append(i)
    double.append((i**2))

result = dict(zip(num,double))

squars = {i:i**2 for i in rang(1,11)}
# =========================
# 19. 다형성 / 추상화
# 문제: Animal 클래스에 move() 추상 메서드 정의
# Dog, Bird 클래스에서 move() 재정의 후 반복문으로 호출
# =========================

class Animal():
    def move(self):
        print("움직인다")

class Dog(Animal):
    def move(self):
        print("뛰어다닌다")

class Bird(Animal):
    def move(self):
        print("날아다닌다")

d =Dog()
B =Bird()

animals = [d,b]
for animal in animals:
    animal.move()

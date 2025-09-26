# 1️⃣ 자료형 / 변수 / 연산
# 문제: 두 수를 입력받아 합, 차, 곱, 나누기 결과를 출력하세요.
# 힌트: input()과 int() 사용

num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요"))

print(f' 두 수의 결과는 합: {num1+num2}, 차:{num1-num2}, 곱: {num1*num2}, 나누기{num1/num2} 입니다')

# 2️⃣ 조건문 / 반복문
# 문제: 1~15 사이 숫자 중 홀수만 출력하고,
# 10 이상이면 "10 이상"이라고 함께 출력하세요.

for i in range(1,16,2):
    if i >= 10 :
        print(i,"10이상")
# 3️⃣ 리스트 / 딕셔너리
# 문제: 리스트 [2,4,6,7,9]에서 짝수만 새로운 리스트로 만들고,
# 인덱스와 값으로 딕셔너리를 생성하세요.
list_a=[2,4,6,7,9]
pair = []
for i in list_a:
    if i % 2 ==0:
        pair.append(i)

dict_pair = {}
for idx,value in enumerate(pair):
    dict_pair[idenx] = value

print(dict_pair)

# 4️⃣ 함수 / *args
# 문제: 여러 숫자를 받아 최대값과 최소값을 반환하는 함수 max_min(*args)를 작성하세요.
# 호출 예시: max_min(3,7,1,9,5) → (최대값, 최소값)

def max_min(*arge):
    maxium = max(args)
    minium = min(args)
    return maxium, minium

result = max_mix(3,7,1,9,5)

print(result)
print(result[0])
print(result[1])

# 5️⃣ 클래스 / 상속 / 다형성
# 문제: Vehicle 클래스 작성, move() 메서드 정의
# Car, Bicycle 클래스 상속 후 각각 다른 move() 출력
# 반복문으로 객체 리스트 순회하며 move() 호출

class Vehicle():
    def move(self):
        print("움직인다")

class Car(Vehicle):
    def move(self):
        print("바퀴로 움직인다")

class Bicycle(Vehicle):
    def move(self):
        print("페달로 돌린다") 
      
a = Vehicle()
b = Car()
c = Bicycle()

list = [a,b,c]
for i in list:
    i.move()

# 6️⃣ property / setter / getter
# 문제: BankAccount 클래스 작성
# balance 속성은 음수 불가, 입금/출금 메서드 작성
# setter로 음수 금액 제한

class BankAccoint():
    def __init__(self,balance = 0):
        self._balance = balance

    @property
    def balance (self):
        return self._balance
    
    @balance.setter
    def balance(self,value):
        if value < 0 :
            print("잔액은 음수가 될 수 없습니다")
        else:
            self._balance = value
    def deposit(self, amount):
        if amount > 0:
            self._balance +- amount
        else:
            print("0이하 금액은 입금할 수 없습니다")
    
    def withdraw(self, amount):
        if 0 < amount <=self.balance:
            self._balance -= amount
        else:
            print("잔액 부족 또는 잘못된 금액입니다")

acc = BankAccount(100)   # 초기 잔액 100
print(acc.balance)       # 100

acc.deposit(50)
print(acc.balance)       # 150

acc.withdraw(70)
print(acc.balance)       # 80

acc.balance = -10        # setter 발동
print(acc.balance)   
    
# 7️⃣ map / filter / lambda
# 문제: 리스트 [3,5,6,8]에서 짝수만 2배로 만들어 출력

even_num = filter(lambda i: i%2 == 0, list_a)
result = map(lambda i :i *2, even_num)
print(list(result))

# 8️⃣ 딕셔너리 컴프리헨션
# 문제: 1~8까지 제곱수를 딕셔너리 {숫자: 제곱} 형태로 출력
squares = {i: i**2 for i in range(1, 9)}
print(squares)
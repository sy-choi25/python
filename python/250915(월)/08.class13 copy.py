# 파이썬 클래스에서 getter setter의 사용법
import random
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def set_age(self,age):
        if age < 0 :    
            print("나이는 음수가 될 수 없습니다.")
        else:
            self.age = age


p = Person("홍길동", 25)
print(p.name)
print(p.age)    
p.name = "김철수"
p.age = 30
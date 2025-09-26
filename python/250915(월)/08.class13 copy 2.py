
# getter-> 객체의 속성 값을 읽어올 때 사용하는 메소드
#  setter->  객체의 속성 값을 변경할 때 사용하는 메소드

import random
class Person:
    def __init__(self, name, age):
        self.name = name 
        self._age = age 
    @property   
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

p1 = Person("홍길동", 25)
print(p1.age)
p1.age = 30
print(p1.age)
print(p1.name)
del p1.name    # name 삭제
print(p1.name) # 에러 'Person' object has no attribute 'name'
# 파이썬 클래스에서 getter setter의 사용법
import random
class Person:
    def __init__(self, name, age):
        self.__name = name #private 변수로 설정
        self.__age = age #ptivate 변수로 설정

a = Person('홍길동',25)
print(a.__name) # 직접 접근(권장되지 않음)
print(a.__age) # 직접 접근(권장되지 않음)

# geter 메소드
def get_name(self):
    return self.__name

def get_age(self):
    return self.__age

# set 메소드
def set_name(self):
    return self.__name

def set_age(self):
    return self.__age


    # 데코레이터를 이용한 setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        self._age = age
p = Person("홍길동", 25)
print(p.name)
print(p.age)    
p.name = "김철수"
p.age = 30
# Q2. Student 클래스를 완성해보세요.
# - 생성자(__init__)에서 name, age를 받아 저장하세요.
# - info_student() 메서드를 만들어 "이름: OOO, 나이: OOO" 형식으로 출력하세요.

students = []
class Student():
    def __init__(self):
        self.name = ' '
        self.age = 0
    
    def info_student(self):
        print(f' 이름: {self.name} 나이 : {self.age}')

s1 = Student()
s1.name = '홍길동'
s1.age = 20
students.append(s1)

s2 = Student()
s2.name = '이순신'
s2.age = 30
students.append(s2)

for stu in students:
    stu.info_student()

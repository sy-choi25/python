# 학생
# 이름, 학생정보를 출력
# 변수 : 이름
# 함수: 학생정보 출력

students = [] # 학생들
def info_student(student):
    print(f' 이름: {student['name']} 나이 : {student['age']}')

# 1) 학생정보 입력
students.append(
    {'name': '홍길동', 'age': 25}
)
students.append(
    {'name': '이순신', 'age': 35}
)    

# 2) 학생정보 입력
def create_student(name,age):
    return {'name':name, 'age': age}


# 모든 학생 출력
for s in students:
    info_student(s)



# 클래스로 입력

students = [] # 학생들
class StudentMng():
    def __init__(self):
        self.name=''
        self.age = 0

    def info_student(self):
        print(f' 이름: {[self.name]} 나이 : {[self.age]}')

s1 = StudentMng()
s1.name = '홍길동'
s1.age = 25
students.append(s1)

s2 = StudentMng()
s2.name = '홍길동2'
s2.age = 27
students.append(s2)

students[0].info_student()
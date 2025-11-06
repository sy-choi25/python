# Q. Student 클래스를 완성하고 학생 정보를 리스트에 저장해보세요.
# 1) 생성자(__init__)에서 name, age를 받아서 저장하도록 작성
# 2) info_student() 메서드로 "이름: OOO, 나이: OO" 형식으로 출력
# 3) 학생 3명을 리스트에 추가하고 반복문으로 출력

students = []  # 학생 리스트

# 클래스 정의
class Student:
    # 여기에 __init__과 info_student() 메서드를 작성하세요
    pass

# 학생 추가
# 예: students.append(Student("홍길동", 20))
# 세 명의 학생 데이터를 추가하세요
# 학생 예시: "홍길동", 20 / "이순신", 30 / "강감찬", 25

# 출력
# for문을 이용해 모든 학생 정보를 출력
students = []
class Student():
    def __init__(self):
        self.name = " "
        self.age = 0
        print(f'이름: {self.name}, 나이: {self.age}')

students.append(Student("홍길동",20))
students.append(Student("이순신",30))
students.append(Student("강감찬",25))

for student in students:
    student.info_student()


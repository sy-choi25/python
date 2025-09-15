# ===============================
# [딕셔너리(dict) 복습 문제]
# ===============================

# ===== 개념 요약 =====
# 1. 딕셔너리 = {key: value} 쌍으로 구성
# 2. 키(key)는 중복 불가, 변경 불가(숫자, 문자열, 튜플 가능)
# 3. 값(value)은 모든 자료형 가능
# 4. CRUD 가능
#    - 읽기: dict[key]
#    - 추가/업데이트: dict[key] = value
#    - 삭제: del dict[key]
# 5. 순환문과 함께 items(), keys(), values() 사용 가능

# ===============================
# [연습 문제 5단계]
# ===============================

# 문제 1️⃣ (기초)
# student = {"name":"홍길동","age":20,"major":"컴퓨터"}
# 'name' 값을 출력해보세요.
student = {"name":"홍길동","age":20,"major":"컴퓨터"}
# 여기에 코드 작성
print("문제1 결과 =", )  

print(student['name'])           # 딕셔녀리 안에 특정 값은 꺼내기 때문에 []로 써준다   


# 문제 2️⃣ (기초-활용)
# student에서 'age' 값을 25로 업데이트 해보세요.
# 업데이트 후 student 전체를 출력해보세요.
# 여기에 코드 작성
print("문제2 결과 =", )

student["age"] = 20
print(student)


# 문제 3️⃣ (중간)
# student에서 'addr' 키로 "서울시 강남구"를 추가하고 출력해보세요.
# 여기에 코드 작성
print("문제3 결과 =", )

student = {"name":"홍길동","age":20,"major":"컴퓨터"}
student["addr"] = "서울시 강남구"
print(student)


# 문제 4️⃣ (중간-응용)
# 두 리스트를 dict로 변환해보세요.
names = ['홍길동','이순신','강감찬']
scores = [100, 99, 98]
students = {}
# for문을 이용해서 names[i]를 키로, scores[i]를 값으로 넣어보세요.
# 여기에 코드 작성
print("문제4 결과 =", students)

#1)
names = ['홍길동','이순신','강감찬']
scores = [100, 99, 98]
students = {}

for i in range(len(names)):
    students[names[i]] = scores[i] 


#2)

for name, score in zip(names, scores):
    students[name] = score

# 문제 5️⃣ (심화)
my_bag = {'필통':'파란색','공책':'수학공책','지갑':'분홍색'}
# 1) '지갑' 값을 '가죽지갑'으로 수정
# 2) '물통':'하얀색' 추가
# 3) '공책' 삭제
# 4) for문으로 key와 value를 모두 출력

for key in my_bag:
    print({key,my_bag[key]})

for key, value in my_bag.item():
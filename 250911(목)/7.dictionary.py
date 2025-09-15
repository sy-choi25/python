# 집합을 이루는 요소: 숫자, 문자, 문자열, 리스트, set, 튜플  # [1, 1.5, "문자", [1,2], {2,3}, (1)]
# dict
# 키와 값의 쌍으로 구성 {key:value, key: value}
# 키는 중복 안됨
# 키는 변하지 않는 자료형만 가능(문자열, 숫자, 튜플)
# CRUD 가능
    # C → Create : 새로 만들기 / 추가
    # R → Read : 읽기
    # U → Update : 수정 / 업데이트
    # D → Delete : 삭제
# 각 요소에 접근할때는 키 값을 접근(인덱스가 아님)

student = {
    "name" : "홍길동",
    "age" : 20,
    "major" : "컴퓨터"
}
# 읽기
print(f"student['name'] = {student['name']}")
# 업데이트                              # 업데이트와 추가 동일. 키 값이 있으면 업데이트, 없으면 추가가 됨
student['name'] = "이순신"
print(f"student = {student}")
# 삭제
del student["name"]
print(f"student = {student}")
# 추가                                  # 업데이트와 추가 동일
student['addr'] = "서울시 강남구"
print(f"student = {student}")
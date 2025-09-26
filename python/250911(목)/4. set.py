# 저금통
list_a = [100, 500, 10, 500, 100, 50, 500, 10]
# 저금통에 있는 동전의 종류 10, 50, 100, 500

# set
set_a = { 1, 2, 3, 1, 2, 3, 1}       # set 의 형태는 set = { }
print(f'set_a = {set_a}')            # 중복을 제거, 나열 순서는 보장되지 않음. 리스트, 튜플과 형태 변경 가능 

# 중복을 제거(허용하지 않는다)
print(set(list_a))

# set는 인덱스 사용 x -> 순서를 보장하지 않음
set_2 = {1, 2}
# print(set_2[0])  set는 인덱스 사용 x -> 순서를 보장하지 않음

set_2.add(3)                 # 값 추가
print(set_2)

set_2.remove(2)              # 값 삭제
print(set_2)  

set_2.pop()                 # 데이터 마지막 데이터 삭제
print(set_2)

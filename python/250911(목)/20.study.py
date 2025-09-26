# ===============================
# [SET 복습 문제 5단계]
# ===============================

# 문제 1️⃣ (기초)
# list_a = [1,2,2,3,3,3,4]
# 중복을 제거하고 set으로 변환해보세요.
list_a = [1, 2, 2, 3, 3, 3, 4]
# 여기에 코드 작성
print("문제1 결과 =",set(list_a) )  

set(list_a)



# 문제 2️⃣ (기초-활용)
# set_b = {10,20,30}
# 안에 20이 있는지 확인해보세요. (in 연산자 사용)
set_b = {10, 20, 30}
# 여기에 코드 작성
print("문제2 결과 =" )

print(20 in set_b)





# 문제 3️⃣ (중간)
# set_c = {1,2}
# 값 3을 추가(add)하고, 다시 2를 제거(remove)해보세요.
set_c = {1, 2}
# 여기에 코드 작성
print("문제3 결과 =", set_c)


set_c.add(3)
set_c.remove(2)
print(set_c)


# 문제 4️⃣ (중간-응용)
# 두 집합 set_d={1,2,3}, set_e={3,4,5}
# 교집합을 구해보세요.
set_d = {1, 2, 3}
set_e = {3, 4, 5}
# 여기에 코드 작성
print("문제4 결과 =", )

set_sum = set_d & set_e
print(set_sum)

# 문제 5️⃣ (심화)
# 랜덤으로 0~10까지의 숫자 6개를 뽑아 list_x를 만들고,
# 또 다른 랜덤 숫자 4개로 list_y를 만들어라.
# 두 리스트를 set으로 변환 후 합집합, 교집합, 차집합을 구하시오.
import random
list_x = random.sample(range(11), 6)
list_y = random.sample(range(11), 4)

set_x = set(list_x)
set_y = set(list_y)

print("문제5 list_x =", list_x)
print("문제5 list_y =", list_y)
# 여기에 코드 작성

import random

list_x = random.sample(range(11),6)
list_y = random.sample(range(11),4)

set_x = set(list_x)
set_y = set(list_y)

set_sum = set_x | set_y 
set_same = set_x & set_y 
set_mi = set_x - set_y

import random

list_x = random.choices(range(11), 6)
list_y = random.choices(range(11), 4)

set_x = set(list_x)
set_y = set(list_y)

set_sum = set_x | set_y       # 합집합
set_same = set_x & set_y      # 교집합
set_mi = set_x - set_y
# 집합 연산 가능

# 1)
import random
list_a = random.sample(range(10),6)
list_b = random.sample(range(10),4)
find_list = []
for a in list_a:                    # 랜덤으로 추출된 list_a 중 a의 값과
    for b in list_b:                # 랜덤으로 추출된 list_b 중 b의 값과
        if a == b:                  # a와 b의 값이 같을 때
            find_list.append(a)     # a의 값을 find_list에 추가
print(f' list_a = {list_a}')
print(f' list_b = {list_b}')
print(f'find_list = {find_list}')

# 2) 중복값이 있을 때
import random
list_a1 = random.sample(range(10),6)
list_b1 = [1,5,4,1,2,1,5,1,7,1]
find_list1 = []
for a in list_a1:                    # 랜덤으로 추출된 list_a 중 a의 값과
    for b in list_b1:                # 랜덤으로 추출된 list_b 중 b의 값과
        if a == b:                  # a와 b의 값이 같을 때
            find_list1.append(a)     # a의 값을 find_list에 추가
print(f' list_a = {list_a1}')
print(f' list_b = {list_b1}')
print(f'find_list = {find_list1}')
print(f'set(find_list) = {set(find_list1)}')   # set을 씌워 중복값 제거





# 13라인에서 set을 사용하지 않고 원래 로직(6~9라인)을 개선해서 
# find_list에 중복값이 저장되지 않도록 

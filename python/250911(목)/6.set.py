# 집합연산이 가능

import random
list_a = random.sample(range(11),6) # 0~10 중복되지 않은 임의의 7개
list_b = random.sample(range(11),4)

# 중복을 허용하면서 0~10 임의의 7 추출
# random.randint(0,10)  -> 임의의 한개

list_c = []
for i in range(7) :         # i의 역할이 없다. 문법을 맞춰주기 위해 i를 썼음.   # for _ in range(7)  -> 같은 표현으로 i 대신 _ 를 넣음
    list_c.append(random.randint(0,10))

# 합집합
    # 연산자 | (파이프 연산자) -> or의 개념
set_a = {1, 2, 3,}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)
    # 메서드 .union()    # .union 처럼 . 뒤에 함수가 나오는 것이 메서드/ 함수는 type() 처럼 바로 오는 것 
union_set = set_a.union(set_b)
print(union_set)

# 교집합
    # 연산자 &   -> and
set_a, set_b = {1,2,3,4}, {2,3,5}
print(set_a & set_b)    
# 메서드 .intersection()
print(set_a.intersection(set_b))

# 차집합
    # 연산자 -  
print(set_a - set_b) 
    # 메서드 .difference()
print(set_a.difference(set_b))
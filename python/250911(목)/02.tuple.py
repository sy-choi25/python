# 원본 데이터 값이 변경됨

def change(obj):
    obj[0] = 100

data = [1,2,3]
change(data)
print(data)

# 

a = 10
b = a
b = 1000
print(f' a={a}, b={b}')                             # b = a 식이여도 a의 값은 변경되지 않음

list_a = [1, 2, 3]
list_b = list_a
list_b[0] = 100
print(f' list_a = {list_a} list_b = {list_b}')      # 리스트는 값들이 변경됨

# 

list_a1 = [1, 2, 3]
list_b1 = list_a1.copy()            # ->list_b = list_a 이렇게 직접사용하지 않고 list_b = list_a.copy()를 사용
list_b1[0] = 100
print(f' list_a1 = {list_a1} list_b1 = {list_b1}') 
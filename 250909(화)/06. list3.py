# 리스트를 선언햡니디
list_a = [1, 2, 3]
list_b = [4, 5, 6]
last_name = '홍'
first_name = '길동'
# 리스트 연산
print(f'list_a + list_b = {list_a + list_b}')
print(f'list_a *2 = {list_a*2}')

print(f'last_name + first_name = {last_name+first_name}')
print(f'last_name * 2 = {last_name*2}')

# 각 위치에 있는 값들을 더할 때
list_c = [
    list_a[0]+list_b[0],
    list_a[1]+list_b[1],
    list_a[2]+list_b[2]
    ]
print(list_c)



# append, insert 함수
# 1. 리스트 선언
list_a = [1, 2, 3]
# 2. 리스트 뒤에 요소 추가(append)
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print("-------------------------------")
#3. 리스트 중간에 요소 추가하기(insert)
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)

# extend 함수
list_a.append([4,5,6]) # 리스트 안에 리스트가 들어간 형태
print(list_a)          
list_a.extend([4,5,6]) # 리스트 뒤에 확장된 형태
print(list_a)

# 아래 세 개의 값은 list_a + [1,2,3,4,5,6] 라는 같은 값을 가짐. 표현형태만 다름
# list_a.extend([4,5,6])
# list_a = list_a +[4,5,6] 
# list_a += [4,5,6] 

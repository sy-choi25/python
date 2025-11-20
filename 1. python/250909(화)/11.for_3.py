# remove
list_a = [1, 1, 1, 2]
# list_a.remove(100)  # 100은 변수에 없기 떄문에 에러 
list_a.remove(1)
print(list_a) # 가장 앞의 1만 지워짐


# 리스트에 있는 1을 모두 제거할 때

# 1. 역순

list_a = [1, 1, 1, 2]

for i in range(4-1, -1, -1):  # 인덱스 순서가 틀어지지 않게 역순으로 확인
    if list_a[i] == 1:
         del list_a[i]
         
print(list_a)


# 2. remove 사용

list_a1 = [1, 1, 1, 2]
for i in range(len(list_a1)):
    if 1 in list_a1:
        list_a1.remove(1)

print(list_a1)


list_a2 = [1, 1, 1, 2,2,2,2,2]
for i in range(len(list_a2)):
    if 1 in list_a2:
        list_a2.remove(1)
    else:
        break               # 더이상 순환하지 않음

print(list_a2)



# 이럴떄 for문보다는 while 이 더 오류가 없다고?

list_b = [1, 1, 1, 2]
while 1 in list_b :
    list_b.remove(1)
print(list_b)
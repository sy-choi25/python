# 중첩 for문2

list_1 = [10, 20, 30]
list_2 = [11, 22, 33]

list_2th = [list_1, list_2]

for i in range(len(list_2th)):
    for j in range(len(list_1)):
        print(f'list_2th[{i}][{j}] {list_2th[i][j]}')



# 리스트의 갯수가 다를 떄
list_1 = [10,20,30]
list_2 = [11,22]

list_2th = [list_1, list_2] 

for i in range(len(list_2th)):         # 외부 반복: i = 0,1
    for j in range(len(list_2th[i])):  # 내부 반복: i번째 리스트 길이만큼
        print(f'list_2th[{i}][{j}]  {list_2th[i][j]}')
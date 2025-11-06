
# 고급 문제 6
# 구구단 2~9단 출력, 가로 방향 출력 (end="\t" 사용)
# 여기에 작성

for j in range(1,10):
    for i in range(2,10):
        print(f'{i} x {j} = {i*j}', end="\t")
    print()
    
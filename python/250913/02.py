# 타이머가 5초동안 지나가고
# 대신 1초의 지연을 줘야함
# 그리고 사용자에게 계속 지속할지 질문
# y 라면 계속하고
# n 라면 중지

import time

count = 0
is_conti = True
while is_conti:
    count += 1
    print(f'{count}초')
    time.sleep(1)
    if count % 5 == 0 :
        answer = input("계속하시겠습니까?(Y/N)").upper()
        if not answer == "Y":
            is_counti = False
            print("프로그램을 종료합니다.")
            break
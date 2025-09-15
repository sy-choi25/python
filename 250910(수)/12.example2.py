# 가위 바위 보 게임 (컴퓨터 vs 휴먼)
# 가위 : 1 , 바위 : 2, 보: 3
# 규칙: 컴퓨터가 임의로 숫자를 선택    # random
# 인간이 숫자를 입력                   # input
# 승패를 기록                           
# 3번마다 계속할 것인지 물어본다       # for

import random
# 1: 가위
# 2: 바위
# 3 보

def get_com_num(start=1, end=3):
     '''
     랜덤값출력(strat~end)
     '''
     return random.randint(start, end)

def get_hum_num():
     return int(input("입력(1:가위 2: 바위 3:보):"))

def check_winner(com_choice, human_choice):
    if com_choice == human_choice:
            print("비겼습니다")
    else:
        if(com_choice == 1 and human_choice == 2) or \
                (com_choice == 2 and human_choice == 3) or \
                (com_choice == 3 and human_choice == 1) :
            print("이겼습니다")
        else: 
            print("졌습니다.")   

import games  # games.py이 폴더에 있는 값을 import

# 랜덤하게 선택한 컴퓨터의 값
com_choice = games.get_com_num()
# 사용자의 값
human_choice = games.get_hum_num()
# 승패 확인
games.check_winner(com_choice,human_choice)




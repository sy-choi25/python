import random

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
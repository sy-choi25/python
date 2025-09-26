#문제
#클래스로 작성된 가위바위보 게임을 수정하세요.
#5판을 진행한 후, 최종 스코어(사용자 승, 컴퓨터 승, 무승부)를 출력

# 사용자에게 가위바위보받기
# 컴퓨터에게 랜덤으로 가위바위보받기
# 총 게임 다섯 번을 진행
# 최종 스코어를 출력한다

import random

class RPSGame():
    def __init__(self):
        self.human_score = 0
        self.computer_score= 0
        self.draw = 0

    def get_comuter_choice(self):
        return random.sample(1,3) 

    def get_human_choice(self)
        choice = int(input("가위:1 , 바위:2, 보:3을 선택하세요"))
        while choice not in [1,2,3]:
            print("잘못 입력했습니다")
            choice = int(input("가위:1 , 바위:2, 보:3을 선택하세요"))
        return choice

    def play_round(self):
        human = self.get_human_choice()
        


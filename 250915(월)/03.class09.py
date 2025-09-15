# 가위바위보 게임을 클래스로 구현하기
# 사용자로부터 입력을 받아 컴퓨터와 대결하는 간단한 가위바위보 게임을 구현
# 사용자는가위바위보 중 하나를 입력하고 컴퓨터는 무작위로 선택
# 게임의 승패를 판단하고 결과를 출력
# 가위는 1, 바위는 2, 보는 3으로 표현
# 이러한 규칙을 클래스로 구현
# 게임이 끝나면 계속할지 물어본다

import random
class RockPaperScissors:
    choices = {1: "가위", 2: "바위", 3: "보"}

    def __init__(self):
        self.user_choice = None
        self.computer_choice = None

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))  # 문자가 입력될 가능성이 있음. 오류발생 케이스
                if choice in self.choices:  # 사용자 입력 숫자의 범위를 체크. 1~3 이외의 숫자를 입력할 경우 else 단계로 넘어가 오류가 발생하고 다시 try 질문으로 돌아감
                    self.user_choice = choice
                    break
                else:
                    print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def get_computer_choice(self):  
        self.computer_choice = random.randint(1, 3)

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "무승부"
        elif (self.user_choice == 1 and self.computer_choice == 3) or \
            return "사용자 승리"
        else:
            return "컴퓨터 승리"
        
    def play(self):
        self.get_user_choice()
        self.get_computer_choice()
        print(f"사용자 선택: {self.choices[self.user_choice]}, 컴퓨터 선택: {self.choices[self.computer_choice]}")
        result = self.determine_winner()
        print(result)

RockPaperScissors().play() 
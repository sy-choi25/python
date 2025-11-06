# 숫자 야구 게임
# 사용자에게 3자리 숫자를 입력받아 컴퓨터가 생성한 3자리 숫자와 비교한다
# 각 자리의 숫자와 위치가 모두 맞으면 "스트라이크", 숫자만 맞으면 "볼", 숫자와 위치가 모두 틀리면 "아웃"을 출력
# 사용자가 숫자를 맞출 때까지 계속해서 입력을 받는다

import random 
class NumberBaseballGame:
    def __init__(self):
        self.number_to_guess = self.generate_number()
        self.attempts = 0

    def generate_number(self):
        digits = random.sample(range(10), 3)
        return ''.join(map(str, digits))

    def guess(self, user_guess):
        self.attempts += 1
        strikes = sum(1 for a, b in zip(user_guess, self.number_to_guess) if a == b)
        balls = sum(1 for digit in user_guess if digit in self.number_to_guess) - strikes
        outs = 3 - strikes - balls
        return strikes, balls, outs
    
game = NumberBaseballGame()
while True: 
    user_input = input("3자리 숫자를 입력하세요: ")
    if len(user_input) == 3 and user_input.isdigit() and len(set(user_input)) == 3:
        strikes, balls, outs = game.guess(user_input)
        print(f"{strikes} 스트라이크, {balls} 볼, {outs} 아웃")
        if strikes == 3:
            print(f"정답입니다! {game.attempts}번 만에 맞추셨습니다.")
            break
    else:
        print("유효한 3자리 숫자를 입력하세요 (중복된 숫자 없음).")
        
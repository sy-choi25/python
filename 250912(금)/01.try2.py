# 오류를 피해가는 행위 -> 예외 처리

# num1= int(input('숫자를 입력하세요:'))
# num2= int(input('숫자를 입력하세요:'))

num1, num2 = map(int, input('공백을 기준으로 두개의 숫자를 입력').split())
calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

# print(f'{num1} + {num2} = {calc_lists[0]}')
# print(f'{num1} - {num2} = {calc_lists[1]}')
# print(f'{num1} * {num2} = {calc_lists[2]}')
# print(f'{num1} / {num2} = {calc_lists[3]}')

print('1. 더하기', end='\t')
print('2. 빼기', end='\t')
print('3. 곱하기', end='\t')
print('4. 나누기')
choice = int(input('원하는 결과를 입력하세요'))
print(f'결과는 = {calc_lists[choice]}')

############
# 위 코드에서 오류 상황 3가지
    # "공백을 기준으로 ~"에 0을 넣으면 오류
    # 0을 넣었을 때 나누기 에러  
    # "원하는 결과" 에 4번을 입력했을 때 인덱스 오류

# try except 구문
try: # 예외가 발생할 가능성이 있는 코드
except: # 예외가 발생했을 떄 실행할 코드
else: # 예외가 발생하지 않았을 때 실행할 코드/ except에 오류가 걸리면 그 케이스는 else를 실행하지 않음. 잘쓰지 않음
finally: # 무조건 실행할 코드/ except에서 오류 생겨도 마지막에 실행함. 잘쓰지 않음
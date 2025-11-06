# try를 이용하여 오류 수정

try:
    num1, num2 = map(int, input('공백을 기준으로 두개의 숫자를 입력').split())
    calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

    print('1. 더하기', end='\t')
    print('2. 빼기', end='\t')
    print('3. 곱하기', end='\t')
    print('4. 나누기')
    choice = int(input('원하는 결과를 입력하세요'))
    print(f'결과는 = {calc_lists[choice-1]}')
except:
    print('오류발생')

print('프로그램 종료')
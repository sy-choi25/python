# 예외객체 - 예외 발생 시 예외 정보가 저장되는 곳

try:
    num1, num2 = map(int, input('공백을 기준으로 두개의 숫자를 입력').split())
    calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

    print('1. 더하기', end='\t')
    print('2. 빼기', end='\t')
    print('3. 곱하기', end='\t')
    print('4. 나누기')
    choice = int(input('원하는 결과를 입력하세요'))
    print(f'결과는 = {calc_lists[choice-1]}')
except Exception as e:                      # 어떤 에러인지 확인 가능  # 디테일하게 알고 싶을 경우 에러의 종류를 Exception 자리에 넣어준다
    print(f' 오류발생 : {e}]')

print('프로그램 종료')


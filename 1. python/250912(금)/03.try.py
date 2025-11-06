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
except ValueError as e:                      
    print(f' 오류발생 : {e}]')
except IndexError as e:                      
    print(f' 오류발생 : {e}]')
except Exception as e:              # Exception이 가장 큰 에러를 담는 명령이기 떄문에 위에 디테이한 에러명으로 에러를 잡고 그 에러 이외의 에러는 Exception에서 잡힘
    print(f' 오류발생 : {e}]')
    print(f'에러종류 {e.__class_.name_}\n 설명:{e}')

print('프로그램 종료')


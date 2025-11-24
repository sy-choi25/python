# [문제 1] 
# 사용자로부터 1~50 사이의 정수를 입력받아 출력하는 get_number() 함수를 작성하세요.
# 잘못된 입력이면 "오류: ..."를 출력하고 다시 입력받도록 하세요.

#1단계
num= int(input('1~50 사이의 정수를 입력하세요'))
print(num)
if 1 <= num <= 50:
    print(f'입력한 값: {num}')
else:
    print('범위를 벗어났습니다')

#2단계
while True:
    try:
        num= int(input('1~50 사이의 정수를 입력하세요'))
        if 1 <= num <= 50:
            raise ValueError('1~50 범위 초과')
    except Exception as e:
        print(f'오류: {e}')
    else:
        break
    
print(f' 입력한 값:{num}')

#3단계
del get_number():   
    while True:
        try:
            num= int(input('1~50 사이의 정수를 입력하세요'))
            if 1 <= num <= 50:
                raise ValueError('1~50 범위 초과')
        except Exception as e:
            print(f'오류: {e}')
        else:
            break
    
print(f' 입력한 값:{num}')

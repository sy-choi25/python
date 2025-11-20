# while 반복횟수가 없다 / for의 경우 횟수를 range에 넣어주니까 횟수가 한정적

import time

count = 0            # 0부터 시작
is_continue = True   # 무한반복
while is_continue: 
    count += 1      # 1씩 증가
    print(f' {count}초') # 1,2,3,4,5...
    time.sleep(1)   # 1초간 지연

    # 5초 단위로 사용자한테 계속 할건지 물어본다 "To be continue(Y/y)

    if count % 5 == 0 :  # 5의 배수일때
        user_input = input('To be continue(Y/y)').upper() # 사용자한테 물어본다. upper은 모두 대문자로 바꿔준다
        if not  user_input =='Y': # 답이 Y가 아니라면
            is_continue = False # 종료
            print("프로그램을 종료합니다.") 
            break # while문(반복문) 종료



# 혼자 연습 (한국 버전)

import time

count = 0
is_counti = True
while is_counti :
    count += 1
    print(f'{count}초')
    time.sleep(1)
    if count % 5 == 0 :
        user_input = input('계속하시겠습니까?(네/ 아니오)')
        if not user_input == '네':
            is_counti = False
            print("프로그램을 종료합니다.")
            break
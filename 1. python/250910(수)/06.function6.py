import time
# 함수의 정의는 반복문보다 위에 있어야 함
def display_second(count):
    count += 1                      # count 1 증가
    print(f'{count}초')
    time.sleep(1)                   # 1초 동안 프로그램 일시정지
    return count                    # 증가된 count 반환

def is_user_continue(count):
      # 5초 단위로 사용자한테 계속 할건지 물어본다 "To be continue(Y/y)
    if count % 5 == 0 :  # 5의 배수일때
        user_input = input('To be continue(Y/y)').upper() 
        if not  user_input =='Y': 
            return False            # 반복 종료 신호 반환
    return True                     # 반복 계속 (True 반환)
        
count = 0            
is_continue = True                  # 반복을 계속할지 결정하는 변수
while is_continue:                  # 반복 조건이 True일 동안 반복
   count = display_second(count) # 1초간격으로 출력
   is_continue = is_user_continue(count) # 5초 단위로 진행여부 판단



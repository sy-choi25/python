# 사용자 입력 처리 함수
# 이름 get_data()
# 파라메터 (매개변수)
    # start : 시작값
    # end : 종료값
    # int_str : 가이드문구
# 사용자의 입력은 input
# return 정수로 변환된 입력값

def get_data(start,end,input_str='입력'):
    while True:                                             # 반복할 수 있도록 while 함수를 사용
        try:
            h_num = int(input(f"{input_str}({start}~{end})"))  # 정수가 아닌 경우, 1~100 범위를 벗어난 경우, 앞뒤 공백이 있는 경우를 오류로 처리
            if not start <= h_num <= end:
                raise ValueError (f'{start}~{end} 범위 초과')
        except Exception as e:
            print(f' 오류 : {e}')
        else:
            return h_num

print(get_data(1,100,'정수'))
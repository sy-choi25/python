# raise 예외 발생하기
try:
    print('정상코드')
    print('예외발생')
    # raise "내가 발생시킨 에러"
    raise ValueError ("테스트")              # 어떤 에러인지 기입 가능
except Exception as e :
    print(f' 에러 : {e}')
    print(f' 에러 : {e.__class__}')          # 에러의 클래스를 알 수 있음
    print(f' 에러 : {e.__class__.__name__}') # 에떤 에러인지 확인 가능

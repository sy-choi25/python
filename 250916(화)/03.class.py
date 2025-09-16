# 정수값이고 주어진 범위를 벗어나면 발생하는 Exception
class OutOfRangeError(Exception):
    def __init__(self, strname):
        super().__init__(strname)
    def show_info(self):
        return '사용자가 정의한 예외입니다'

try:
    number = 100
    if not 0 <= number <= 10:
        raise OutOfRangeError ('0과 10사이를 벗어났습니다')
#except ValueError:         # 에러명 맞춰줘야 함. 아니면 에러발생 출력안됨
#    print('에러발생')
    int('dfshdfsdd')
except OutOfRangeError as e:
    print(e.show_info())
except ValueError as e:
    print(e)

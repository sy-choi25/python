# 함수
# 함수명 add
# 파라메터는 2개 op1, op2
# 결과를 반환한다

# 생성
# 1)
def add(op1, op2):
    return op1 + op2
# 2) result에 값을 담아도됨
def add(op1, op2):
    result = op1 + op2
    return result
    
# 사용   # 두가지 모두 가능
add(10,20)
numbers = [add(10,20), add(10,2)]


# 매개변수를 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수명 : data

def show_number(data):
    print(f'numbers = {data}')

show_number(add(10,20))


def show_number(data):
    return f'numbers = {data}'


def hello(name):
    result = len(name)
    return result

print(hello("안녕하세요"))


def hello(name):
    return len(name)

print(hello("안녕하세요"))
# 람다가 사용되지 않는 상황
def add(a,b) :
    return a+b

def minus(a,b):
    return a-b

def calc(func, a, b):
    return func(a,b)

print(calc(add,1,2))

# 람다를 사용하면 한줄로 표현 가능
print(calc(lambda a,b : a+b, 1,2))
print(calc(lambda x,y : x*y, 10,20))






















































































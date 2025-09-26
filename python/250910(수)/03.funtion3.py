# 다양한 매개변수
 # 기본매개변수 default parameter

def myAdd(num1, num2):
    return num1 + num2
result = myAdd(10,20)
print(f'result = {result}')

# 2)
def myAdd(num1, num2=0):  
    return num1 + num2
result = myAdd(10)         # num2=0 을 넣어주면 값이 없을 경우 0으로 로직 실행
print(f'result = {result}')

# 3)
def myAdd(num1, num2=0, num3): # 기본매개변수는 항상 마지막에 와야함. 갯수는 상관없지만 뒤에 부터 채워야함
    return num1 + num2 + num3
result = myAdd(10,20)
print(f'result = {result}')

# 4)
def myAdd(num1, num2=0, num3=0): 
    return num1 + num2 + num3
result = myAdd(10,20)
print(f'result = {result}')

# 5)
def myAdd(num1=0, num2=0, num3=0):
    return num1 + num2 + num3
result1 = myAdd()                       # result1,2,3,4 모두 가능
result2 = myAdd(1)
result3 = myAdd(1,2)
result4 = myAdd(1,2,3)
print(result1,result2,result3, result4)
# 매개변수o, 반환값o
# 매개변수o, 반환값 x
# 매개변수x, 반환값 o
# 매개변수x, 반환값 x

# 매개변수o, 반환값o
def myCalc(num1, num2):
    result = num1 * num2
    return result

print(myCalc(3,4))

# 매개변수x, 반환값 x
def say_hello():
    print('안녕하세요') # print 할때 print(say_hello)가 아닌, print(say_hello())로 해서 None이 나와야함

say_hello() # -> 안녕하세요
print(say_hello()) # -> None

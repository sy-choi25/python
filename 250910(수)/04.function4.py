# 가변 매개변수
 # 함수정의 할 떄, 매개변수의 개수를 지정하지 않습니다.
 # 함수내부에서는 리스트로 간주합니다.
 # 함수를 호출하는 쪽에서는 1,2,3,4 or 1,2,3,4,5,1,4,5

# 1)
def myFunc1(arge):
    for i in arge:
        pass

datas = [10,20,50,60]
  # 1. myFunc1(datas)
  # 2. myFunc1(10,20,50,60) # 이 식은 에러. arge는 값이 하나이기 떄문에 

# 2)
def myFunc1(*arge):   # 앞에 *를 붙이면 리스트 데이터로 받을 수 있음
    for i in arge:
        pass

myFunc1(10,20,50,60)

# 3)
def myFunc1(arge):  
    for i in arge:
        pass

myFunc1([10,20,50,60])  # 이렇게도 가능, 리스트 데이터 하나


# 언팩킹
a,b= [10, 20]
print(f'a={a}')
print(f'b={b}')
# enumerate()  , zip(),  .items()   .keys()  .values()
# map(), 정렬  --> 람다함수를 적용  
# 함수의 파라메터 - 키워드파라메터, 가변 키워드 파라메터


# enumerate()
# 목적: 리스트(또는 다른 반복 가능한 객체)를 순회할 때, 원소와 함께 인덱스(index)도 동시에 얻고 싶을 때 사용
# for index, value in enumerate(리스트, start=0):
    #실행문
# index → 인덱스 번호 (기본은 0부터 시작)
# value → 해당 인덱스의 원소 값
# start → 인덱스를 몇부터 시작할지 지정 가능 (기본값 0)

list_a = ['사과','포도','딸기']
for idx,data in enumerate(list_a):
    print(f'idx = {idx}   data = {data}')

# zip()  두개의 리스트 또는 집합을 각 원소별로 묶어준다
names = ['홍길동','이순신']
ages = [25,35]
print(  list(zip( names,ages  ))  )  # [('홍길동', 25), ('이순신', 35)]
print(  dict(zip( names,ages  ))  )  # {'홍길동': 25, '이순신': 35}
for name,age in zip(names,ages):
    print(f'name:{name}, age:{age}')

# .items()
dict_1 = {'취미':'수영','좋아하는 음식':'떡볶이'}  
print(f'dict_1 = {dict_1}')
print(f'.keys() = {dict_1.keys()}')
print(f'.values() = {dict_1.values()}')
print(f'.items() = {dict_1.items()}')

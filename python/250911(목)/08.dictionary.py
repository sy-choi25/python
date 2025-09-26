# list, set, tuple, dict
result = dict([['name','홍길동'], ['age', 20]])
print(type(result))
print(result)
# 두개의 리스트 한개는 키에 해당하는 값들의 집합
# 다른 하나는 값에 해당하는 집합
# 이것을 dict 구조로 만드려면

names = ['홍길동', '이순신', '강감찬']
scores = [100, 99, 98]
students = {}

# 비어있는 dict 변수를 생성
# 변수 ['키'] = 값 형태로생성 - 순환문을 통해서

# 방법1
count = 0
for name in names:
    students[name] = scores[count]
    count += 1

# 방법2
for i in range(len(names)):
    students[names[i]] = scores[i]
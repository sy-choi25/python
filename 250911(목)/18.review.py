# 딕셔너리
    # .items()/ .keys() / .values()
dict_1 = {
    '국어' :100,
    '수학' : 80,
    '영어' : 88
}


print(dict_1)
print(f' .keys() = {dict_1.keys()}')
print(f' .values() = {dict_1.values()}')
print(f' .items() = {dict_1.items()}')


# 정렬
    # sorted()
print(dict_1.items())
print(dict(sorted(dict_1.items(), key=lambda data: data[1])))
print(dict(sorted(dict_1.items(), key=lambda data: data[1], reverse=True)))

# max 
    # max()
scores = {'국어': 80, '영어': 75, '수학': 95}  # 과목별 점수를 담은 딕셔너리

print(max(scores))  # '영어' → key 기준으로 가장 큰 값(한글 사전 순)
print(max(scores, key=scores.get))  # '수학' → value가 가장 큰 key
print(scores[max(scores, key=scores.get)])  # 95 → value가 가장 큰 값

# enumerate
    # 순환문에서 리스트를 감싸면 (인덱스, 리스트의 값)
fruits = ['사과', '바나나', '체리']                       # 리스트 생성
for i, fruit in enumerate(fruits):                     # enumerate: 인덱스(i)와 값(fruit)을 동시에 얻음
    print(i, fruit)                                    # 인덱스와 값 출력

for i, fruit in enumerate(fruits, start=1):           # start=1: 인덱스를 1부터 시작
    print(i, fruit)                                    # 1부터 시작하는 인덱스와 값 출력

# zip
    # 여러개의 자료구조 iterable 들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과', '배')
    # [(1, '사과'), (2, "배")]



# map()
    # iterable한 객체의각 요소에 특정 함수를 적용   
    # map (int, ['1', '2'])   -> [1,2]    # 필요하면 람다함수를 이용해 함수를 만들어줌
    
numbers = [1, 2, 3, 4, 5]                       # 숫자 리스트 생성
squared = map(lambda x: x**2, numbers)         # map: 각 요소에 lambda x: x**2 적용
print(list(squared))                            # map 객체를 리스트로 변환 후 출력

a = [1, 2, 3]                                  # 리스트 a
b = [4, 5, 6]                                  # 리스트 b
result = map(lambda x, y: x + y, a, b)        # map: a와 b 각 요소를 더함
print(list(result))                             # 결과: [5, 7, 9]



'''
import collections
datas = [1, 1,1,1,2,1,3,4,1,2,4,1]
print(collections.Counter(datas))
'''
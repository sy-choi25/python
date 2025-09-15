# map() 자료구조 각 요소의 특정 함수를 적용
str_number = ['1', '10', '100']
print(str_number)
print(list(map(int, str_number)))

scores = input('국어 영어 수학 점수를 공백을 기준으로 입력하세요')
scores = scores.split()
kor, eng, math = map(int, scores)
print(kor +eng + math)   # 문자열로 들어감


list_2 = [10, 20, 30]
# 각 원소에 x 2

def test (data):
    return data * 2
print(list(map(test, list_2))) 

# 위와 같은 것을 람다함수로 바꿀 때
print(list(map(lambda data:data*2, list_2))) 
# 람다함수

# 문제 1
# 두 수를 입력받아 곱한 결과를 반환하는 람다 함수를 작성하세요.
# 예시: print(multiply(3, 4))  # 출력: 12

#multiply = None  # 여기에 lambda 식 작성
#print(multiply(3, 4))


multiply = lambda a,b : a*b
print(multiply(3, 4))

# 문제 2
# 문자열을 입력받아 길이를 반환하는 람다 함수를 작성하세요.
# 예시: print(str_length("Python"))  # 출력: 6

#str_length = None  # 여기에 lambda 식 작성
#print(str_length("Python"))

# 람다함수형으로 변경
str_length = lambda name : len(name)

# 문제 3
# 리스트 안의 숫자를 제곱한 값으로 변환하는 람다 함수를 작성하세요.
# 힌트: map() 함수와 함께 사용
# 예시: print(list(squared_numbers))  # 출력: [1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = None  # 여기에 map과 lambda를 조합해서 작성
#print(list(squared_numbers))

# map(함수, 반복가능한자료)

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))   # [1, 4, 9, 16, 25]
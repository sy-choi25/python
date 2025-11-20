# 리스트
 # 여러가지 자료를 저장할 수 있는 자료
 # 대괄호 내부에 자료들을 넣어 선언

age = 20
array = [273,23.3, 32, 103, "안녕하세요", age, True, False]  # age는 선언한 값인 20으로 변환되어 출력
print(array)
print(array[4]) # '안녕하세요'만 print 할 때

# array2에 array를 넣었을 때
array2 = [100, array]
print(array2)
print(array2[1][4])  # '안녕하세요'만 print 할 때


temp = [
    [1, 2],     # temp[0]
    [10, 20],   # temp[1]  # 20이라는 숫자를 도출하고 싶을 때 temp[1][1] / temp[1,1]이라는 표현은 틀림
    [30, 40],   # temp[2]
]

# 실습
list_a = [273,23.3, 32, 103, "문자열", True, False]
list_a[0] 
list_a[1]
list_a[2]
list_a[1:3]
print(list_a[1:3]) # 결과로 [23.3, 32] 도출할 때
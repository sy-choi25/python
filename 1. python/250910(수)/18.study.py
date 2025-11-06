# [개념확인] 1부터 20까지 숫자 중 3의 배수만 출력하기

three = []
for i in range(1,21):
    if i % 3 == 0:
        three.append(i)
print(three)

# [응용(초급)] 1부터 50까지 숫자 중 짝수의 합을 구해서 출력하기

pair = []
for i in range(1,51):
    if i % 2 ==0:
        pair.append(i)
print(sum(pair))

# [중급] 1부터 100까지 숫자 중에서
# 3과 5의 공배수만 리스트에 모아서 출력하고,
# 그 개수도 함께 출력하기

three1 = []
for i in range(1,101):
    if i % 15 == 0:
        three1.append(i)
print(f' 3과 5의 공배수는 {three1}이고, 갯수는 {len(three)}개 입니다')


# [개념확인] 문자열 "Python"에서 첫 글자와 마지막 글자를 출력하기

list_a = "Python"
print(list_a[0],list_a[-1])

# [응용(초급)] 사용자에게 문자열을 입력받아,
# 그 문자열이 몇 글자인지 출력하기

list_b= input("문자를 입력해 주세요")
print(len(list_b))

# [중급] 사용자에게 문자열을 입력받아,
# 그 문자열에서 'a'가 몇 번 등장하는지 출력하기
# (대소문자 구분 없이 세어보기)

# 오답
list_b= input("A가 들어가는 영어단어를 입력해주세요")
list_aa=[]
for ch in list_aa:
    if ch == "a" or ch =="A":
        list_aa.append(ch)
print(len(list_aa))

# 정답
list_b = input("A가 들어가는 영어 단어를 입력해주세요: ")
count = list_b.lower().count("a")   # 전부 소문자로 바꾼 뒤 'a' 개수 세기
print(count)

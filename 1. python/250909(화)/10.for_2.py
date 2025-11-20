# 0~100 사이의 랜덤한 숫자 10개를 리스트로 저장
import random
numbers = random.sample(range(100),10)

# 짝수만 출력
print(numbers)

# numbers 에 있는 데이터 중에 짝수만 찾아서 새로운 리스트에 저장
# 1. 리스트를 순환
# 2. 순환하면서 각 데이터가 짝수인지 판단
# 3. 짝수이면 미리 준비한 빈 리스트에 추가
# 4. 모든 순환이 끝나면 (for문이 끝나면) 준비한 리스트를 출력하고 len()을 이용해 갯수 확인

even_numbers = []                   # 빈 리스트를 만들어 준다
for i in numbers:                   # numbers 리스트의 변수(들을 반복
    if i % 2 == 0:                  # 2로 나누어 떨어진다 -> 짝수를 의미
        even_numbers.append(i)      # 빈리스트(even_numbers)에 짝수인 변수(i)를 추가(append)

print(f'짝수들의 집합 : {even_numbers}, 갯수 : {len(even_numbers)}')


list_a = [0, 1,2,3,4,5,6,7]
list_a.remove(3) # 제일 먼저 만나는 3의 값을 지워줌
list_a.pop(3) # 3번쨰 값을 지움





# 홀수만 출력 (혼자 연습)
zip_numbers = []            # 홀수들의 집합을 zip_numbers 로 선언
for i in numbers:
    if i % 2 != 0 :         # 2로 나눴을 때 0 과 같지 않다. 즉 나머지가 있는 홀수이다
        zip_numbers.append(i)
print(f'홀수들의 집합 : {zip_numbers}, 갯수 : {len(zip_numbers)}')
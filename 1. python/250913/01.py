# 0~100 사이의 랜덤한 숫자 10개를 리스트로 저장
# numbers 에 있는 데이터 중에 짝수만 찾아서 새로운 리스트에 저장
# 1. 리스트를 순환
# 2. 순환하면서 각 데이터가 짝수인지 판단
# 3. 짝수이면 미리 준비한 빈 리스트에 추가
# 4. 모든 순환이 끝나면 (for문이 끝나면) 준비한 리스트를 출력하고 len()을 이용해 갯수 확인

import random

numbers = random.sample(range(1,101),10)
pair = []
for i in range(11):
    if i % 2 == 0:
        pair.append(i)

print(f' 짝수는 {pair}이고, 갯수는 {len(pair)}')

# 홀수를 출력

import random
numbers2 = random.sample(range(1,101),10)
unpair = []

for i in range(11):
    if i % 2 != 0:
        unpair.append(i)


print(f' 홀수는 {unpair}이고, 갯수는 {len(unpair)}')



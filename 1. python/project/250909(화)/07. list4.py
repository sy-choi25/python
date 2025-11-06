# 랜덤 라이브러리 가져오기
import random  # import는 파이썬 내에서 이미 지정되어 있는 라이브러리를 가져오는 것
               # import ramdom 이라고 먼저 선언해줘야 라이브러리를 쓸 수 있고 
               # 그렇지 않을 경우에는 ramdom을 변수로 사용할 수 있음

# 랜덤 라이브러리 중에서 sample 함수를 호출
random_numbers = random.sample(range(100),5) # 0~99까지의 숫자 중에 5개를 추출해서 변수(random_numbers)에 담아주겠다는 의미/ 예제 숫자를 랜덤하게 뽑기 위해서
print(random_numbers)

# 0~10 중에 랜덤하게 정수인 숫자 하나를 뽑는 것
random_int = random.randint(0,10)

random_numbers.append(random_int)

# 50이 포함되어 있는지 확인
print(50 in random_numbers)
print(random_numbers)



print('-'*50)



# 삭제 - del 키워드, pop() 함수
# [1] del       # del list[인덱스] → 해당 위치 요소 삭제, 반환값 없음
del random_numbers[0] # 어떤 것을 삭제하는지 알 수 없음. 
print(random_numbers)

# [2] pop       # list.pop(인덱스) → 해당 위치 요소 삭제 + 그 값을 반환
random_numbers.pop(0) # 삭제하는 데이터 값을 알 수 있음. 
print(random_numbers)
removed_number = random_numbers.pop(0) # pop은 가능하나 del은 삭제한 값을 정의할 수 없음. 에러
print(removed_number) # 삭제하는 데이터 값을 알 수 있음. / insert 함수로 삭제한 값 복원 가능

# [3] remove    # list.remove(값) -> 같은 값이 여러개면 제일 앞에 값만 삭제

# 리스트.clear() # 모두 삭제 하는 메소드


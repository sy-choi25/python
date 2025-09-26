# 선거 시스템
# 유권자들은 기호로 투표 진행 결과를 리스트에 저장
# EX) 1, 2, 3...
# 투표는 순환문을 이용해서 유권작 10명이라면 10번 순환하면서 후보자 1~5번 선택
# [1,2,1,2,3,4,1,5,1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력

candidate = ['홍길동', '이순신', '강감찬', '율곡', '신사임당']
vote = []
counts = 10
result = {}
# for _ in counts:
#   vote.append(int(input("투표를 하세요(1~5):")))
vote = [1, 2, 3, 4, 2, 2,1,2,2,4]
print(f'vote = {vote}')
#dict  기능사용

for i in vote : #1~5
    if i in result:
        result [i] += 1
    else:
        result[i] = 1
print(f'result = {result}')

def find_max(key):

# 키의 값을 가져올 때 
# 1) 딕셔너리 변수['키값']   -> 없으면 에러 발생
# 2) 딕셔너리변수.get('키값') -> 없으면 None

print(result.get[20,1])
print(max(result,key=result.get))


#

cadidate = ['홍길동','이순신','강감찬','율곡','신사임당']  # 후보자 리스트
vote = []  # 투표 결과를 저장할 리스트
counts = 10  # 유권자 수
result = {}  # 투표 결과를 카운트할 딕셔너리

# 실제 입력 대신 테스트용 투표 데이터
vote = [1,2,3,4,2,2,1,2,2,4]  # 유권자 투표 결과
print(f'vote = {vote}')  # 투표 결과 출력

for i in vote:
    if i in result:
        result[i] += 1  # 이미 존재하면 1 증가
    else:
        result[i] = 1   # 없으면 1로 초기화
print(f'result = {result}')  # 후보별 득표수 출력

max_key = max(result, key=result.get)  # 최대 득표 후보 키 가져오기
print(f'당선자 : {cadidate[max_key-1]} 득표수 : {result[max_key]}')  # 당선자와 득표수 출력



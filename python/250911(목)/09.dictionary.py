# 딕셔너리 생성
# 딕셔너리에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제
# 딕셔너리 특정 키의 데이터를 수정

# enumerate(), zip (), .items() .keys() .values()
# map(), 함수의 파라메터 - 키워드파라메터, 가변 키워드 파라메터

my_bag ={'필통' : ' 파란색' , '공책' : "수학공책", "지갑" : "분홍색"}
print(my_bag)
# 가방에서 필통을 꺼내서 출력
print(my_bag['필통'])
# 가방에서 공책을 꺼내서 출력
print(my_bag['공책'])
# 지갑이 오래돼서 '가죽지갑'으로 변경
my_bag['지갑'] = "가죽지갑"
print(my_bag)
# '하얀색' 물통 추가
my_bag['물통'] = "하얀색"
print(my_bag)
# 공책을 다써서 버리기
del my_bag["공책"]
print(my_bag)

# 순환문과 연걸
for i in my_bag:
    print(f' key = {i} value = {my_bag[i]}')
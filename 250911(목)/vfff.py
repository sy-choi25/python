# ===============================
# 📌 어제 배운 내용 복습 문제
# ===============================

# [문제 1] enumerate()
fruits = ['사과', '바나나', '포도']
# TODO: enumerate()를 사용해서 "0 - 사과" 형식으로 출력해보세요.

for idx,fruits in enumerate(fruits):
    print(f'{idx} - {fruits}')

# [문제 2] zip()
names = ['홍길동', '이순신', '강감찬']
ages = [20, 30, 40]
# TODO: zip()을 이용해 (이름, 나이) 튜플 리스트를 출력해보세요.
# TODO: zip()을 dict로 변환해서 출력해보세요.

print(tuple(zip(names,ages)))
print(type(tuple(zip(names,ages))))

# [문제 3] 딕셔너리 메서드
dict_1 = {'취미':'등산','좋아하는 음식':'치킨'}
# TODO: .keys(), .values(), .items() 각각 출력해보고 차이를 주석으로 설명해보세요.

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

# [문제 4] 정렬 & 람다
scores = {'철수':90,'영희':85,'민수':95}
# TODO: max()와 key=scores.get을 이용해서 최고 점수를 받은 사람을 출력해보세요.
# TODO: 점수를 기준으로 오름차순 정렬된 리스트를 출력해보세요.

high = max(scores,key=scores.get)
print(high)
print(sorted(scores.items(), key=lambda x: x[1]))
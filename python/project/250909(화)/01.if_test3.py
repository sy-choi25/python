# 명령어는 모두 실행
# 조건문을 이용하면 특정 명령문은 실행되지 않게 할 수 있다
# 조건문은 
# if 조건 :             # ':'을 꼭 넣어준다
# 들여쓰기를 해서 if 하위 명령어로 만든다 -> 블럭
age = 20
if age >= 18 :
    print('성인입니다.')
    print('조건문은 True 입니다.')
    #
    #
    #
print('if와 상관없는 명령어')


# 조건에 맞으면 합격 그렇지 않으면 불합격
score = 80
if score >= 60:
    print('합격')
else:
    print('불합격')

# if, elif, else 조건문
temperature = 25
if temperature > 30 :
    print('덥다') 
elif temperature > 20: # 범위에 <30 (30미만)을 넣지 않아도 됨. 
                       # 이미 상위 if 조건에서 이 부분을 제외하기 때문
    print('따뜻하다')
elif temperature > 10:
    print('시원하다')
else:
    print('춥다')

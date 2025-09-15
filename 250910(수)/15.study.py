# 문제 1
# 두 수를 입력 받아 큰 수를 반환하는 함수 get_max를 만들어보세요.

#print(get_max(7, 12))  # 결과: 12

def get_max(a,b):
    if a> b:
        return a
    else:
        return b
    
print(get_max(7,12))


# 문제 2
# 이름을 입력 받아 "OO님, 오늘도 화이팅!"을 출력하는 함수 cheer를 만들어보세요.
#cheer("소영")  # 출력: 소영님, 오늘도 화이팅!

def cheer(name):
    print(f'{name}님, 오늘도 화이팅! ')

cheer("소영")

# 문제 3
# 상수값으로 3.14159를 반환하는 함수 get_pi_value를 만들어보세요.
#print(get_pi_value())  # 결과: 3.14159


def get_pi_value():
    pi = 3.14159
    return pi

print(get_pi_value())

# 문제 4
# 함수 호출 시 "오늘 하루도 즐겁게 코딩합시다!"를 출력만 하는 함수 coding_day를 만들어보세요.
# coding_day()  # 출력: 오늘 하루도 즐겁게 코딩합시다!

def coding_day():
    print("오늘도 하루도 즐겁게 코딩합시다")

coding_day()

# 문제 5
# 세 수를 입력 받아 합계를 반환하는 함수 sum_three를 만들어보세요.
# print(sum_three(3, 5, 7))  # 결과: 15

def sum_three(a, b, c):
    return a+b+c

print(sum_three(3, 5, 7))


# 문제 1 매개변수 o, 반환값o
# 두 수를 입력 받아 작은 수를 반환하는 함수 get_min을 만들어보세요.
# 예시: print(get_min(7, 12))  # 결과: 7

def get_min(a,b):
    if a>=b:
        return b
    else:
        return a

print(get_min(7, 12)) 

# 문제 2 매개변수 o, 반환값x
# 이름을 입력 받아 "OO님, 오늘도 힘내세요!"를 출력하는 함수 cheer_up을 만들어보세요.
# 예시: cheer_up("소영")  # 출력: 소영님, 오늘도 힘내세요!

def cheer_up(name):
    print(f'{name}님, 오늘도 힘내세요')

cheer_up("소영")

# 문제 3 매개변수 x, 반환값o
# 상수값으로 9.8을 반환하는 함수 get_gravity를 만들어보세요.
# 예시: print(get_gravity())  # 결과: 9.8

def get_gravity():
    grav = 9.8
    return grav

print(get_gravity())

# 문제 4 매개변수 x, 반환값x
# 함수 호출 시 "코딩은 재미있습니다!"를 출력만 하는 함수 coding_fun을 만들어보세요.
# 예시: coding_fun()  # 출력: 코딩은 재미있습니다!

def coding_fun():
    print("코딩은 재밌습니다")

coding_fun()

# 문제 5 매개변수 o, 반환값o
# # 세 수를 입력 받아 곱을 반환하는 함수 multiply_three를 만들어보세요.
# 예시: print(multiply_three(2, 3, 4))  # 결과: 24

def multiply_three(a,b,c):
    return a*b*c

print(multiply_three(2, 3, 4))
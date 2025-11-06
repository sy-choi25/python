list_a = [1, 2, "문자열", True, False]
print(list_a[2][2])                 # '열'을 도출
print(list_a[:])                    # 원본 복사
print(list_a[:3])                   # 문자열까지 도출
print(list_a[3:])                   # 참, 거짓 도출
print(list_a[-1])                   # 맨 뒤의 변수 도출
print(list_a[-2:])                  # 참, 거짓 도출
# start index : end index -1 : 1    # 여기서 마지막 1은 스텝을 나타냄. 한개씩 순서대로 도출된다는 것이 생략되어 있음
print(list_a[::2]) # 두 스텝씩 도출 
print(list_a[::-1])                 # 역순으로 출력


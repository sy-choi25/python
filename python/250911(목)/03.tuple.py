# 튜플와 리스트는 서로 변경이 가능하다     
# 튜플 -> 리스트, 튜플 <- 리스트 모두 가능 튜플 = 튜플(리스트), 리스트(튜플) = 리스트

list_a = [ 1, 2, 3]
tuple_a = (10, 20, 30)
print(f'type(list_a = ) = {type(list_a )}')
print(f'type(tuple_a = ) = {type(tuple_a) }')

print(type(tuple(list_a)))  # 리스트가 튜플로 타입변경
list_a = tuple(list_a)      # list_a라는 변수를 아예 튜플로 다시 저장
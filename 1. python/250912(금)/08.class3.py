class People():
     def __init__(self):                # 생성자 __int__  사용하면 객체가 자동으로 만들어짐. 따로 메서드를 호출하지 않아도 됨
          self.name = None              # 아래 self를 이용하여 변수 선언
          self.age = None
          self.addr = None
          print('생성자 호출')

print('h1 객체 생성전')
h1 = People()
print('h1 객체 생성후')
print(h1.addr)

# 생성자 필요 -> 인스턴스 변수 생성 및 초기화
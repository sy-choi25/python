class People():
     def make_instance(self):
          self.name = None
          self.age = None
          self.addr = None

h1 = People()           # People 클래스의 인스턴스 h1 생성. 하지만 아직 name, age, addr 속성이 없음.
h1.make_instance()      # make_instance() 메서드가 실행되면서 h1 객체에 name, age, addr 속성이 생성되고 None이 들어감.
print(h1.addr)
h2 = People()
print(h2.addr)

# 생성자 필요
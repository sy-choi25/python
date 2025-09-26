# 상속의 정의
# 상속은 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 것을 의미
# 상속을 통해 코드의 재사용성을 높이고, 계층적인 관계를 표현할 수 있음
# 상속의 기본 문법
class 부모클래스:
    def 부모메서드(self):
        print("부모 메서드 호출")

class 자식클래스(부모클래스):
    def 자식메서드(self):
        print("자식 메서드 호출")

# 부모클래스
class Parents():               #() 생략가능
    def __init__(self, name):
        self.p_name = ''    # 매개변수 name은 사용하지 않음. 홍길동은 속성에 저장되지 않았다
        print('부모생성자')
    def parents_method(self):
        print('부모클래스 메소드')

# 자식클래스        
class Child(Parents):
    def __init__(self, name, age):
        Parents.__init__(self,'홍길동') # 원래 생성자 호출은 안되지만 자식클래스에서의 부모클래스 호출 가능. 단 클래스 안에서만
        self.age = age
        print('자식생성자')

    def child_method(self):    
        print('자식클래스 메소드')   

# Child 클래스 객체 c
c = Child('홍길동', 20)    # Child 클래스에 c객체 추가. __init__ 생성자로 하는 과정이 생략되어 있음
print(c.p_name, c.age)

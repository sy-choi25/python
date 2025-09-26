from abc import ABC, abstractmethod

class Parents(ABC):
    def make_money(self):
        raise NotImplementedError
    
    @abstractmethod             # 추상화, 자식클래스에서 부모 클래스를 사용하려면 무조건 값이 있어야 가능. 공통적인 메소드를 갖도록 강제 가능
    def save_money(self):
        print('저축')
    
class Child(Parents):
    def make_money(self):       # 부모의 make_money 재정의 (override)
        print('장사')

    def save_money(self):               # 반드시 구현해야 함. 아니면 객체를 만들 수 없음
        print('투자')

c = Child()         # 부모의 추상메서드를 상속 받으면 클래스에서 반드시 재정의 안하면 객체 생성 불가
c.make_money()      # 다형성  # 자식클래스에서 재정의하지않으면 예외발생하도록 설계

    
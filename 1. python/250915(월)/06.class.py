# 상속: 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스 만드는 것
# isinstance() :  -> 인스턴트 변수가 맞는지 타입을 물어볼 때 사용. 
#                    상속 관계에 따라서 객체가 어떤 클래스를 기반으롤 만들었는지 확인 할 수 있게 해주는 함수
#                    객체가 특정 클래스의 인스턴스(객체)인지 확인하는데 사용합니다.
# 사용하는 이유
# 1) 타입확인 : 함수나 매서드가 특정 클래스의 인스턴스인지 확인할 수 있음
# 2) 다형성 지원: 상속 관계에 있는 클래스들 간에 공통된 인터페이스를 제공할 때, isinstance()

class Student():
    def study(self):
        return "공부 중입니다"
    
class Teacher():
    def teach(self):
        return "가르치는 중입니다."
    
# 리스트에 어떤 객체가 있는지 모를 때 특정 인스턴스만 기대할 수 없다
peoples = [Student(), Teacher(), Student()]
# peoples[0].teach()  => 에러 Student()에 teach라는 객체가 없음
if isinstance(peoples[0],Student):
    print(peoples[0].study())
else:
    print(peoples[0].teach())




class Student():
    def study(self):
        return "공부 중입니다"
    
class Teacher():
    def teach(self):
        return "가르치는 중입니다."
    
# 리스트에 어떤 객체가 있는지 모를 때 특정 인스턴스만 기대할 수 없다
peoples = [Student(), Teacher(), Student()]
# peoples[0].teach()  => 에러 Student()에 teach라는 객체가 없음
del peoples[0]   # 0번째를 삭제하면 study객체가 지워져서 가르치는 중입니다 가 출력
if isinstance(peoples[0],Student):
    print(peoples[0].study())
else:
    print(peoples[0].teach())


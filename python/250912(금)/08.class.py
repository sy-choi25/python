
# 클래스 변수 vs 인스턴스 변수

class StudentMng():             # 괄호 없이 사용 가능
    name = '홍길동'             # 클래스 변수
    def make_instance(self):
        self.age = 0
                      
s1 = StudentMng()
s2 = StudentMng()
s3 = StudentMng()
s4 = StudentMng()

print(s1.name, s2.name, s3.name)
s1.name = '강감찬'              # 인스턴스 변수
StudentMng.name = '이순신'      # 클래스 변수
print(s1.name, s2.name, s3.name)


#인스턴스에 없는 속성 → 클래스 변수를 찾아감
#인스턴스에 같은 이름의 속성을 새로 만들면 → 그때부터는 클래스 변수를 가리지 않고 자기 것만 씀
#클래스 변수를 바꾸면 → 인스턴스 변수 없는 객체들만 영향을 받음
#인스턴스 변수는 객체 개인 소유.
#클래스 변수는 모든 객체가 공유.
#같은 이름이면 인스턴스 변수가 우선된다.

# 클래스 변수는 모든 객체가 참조하는 변수
# 그러나 객체가 변수를 재할당 받으면 해당 객체는 더이상 참조하지 않음


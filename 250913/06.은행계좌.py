class BankAccount:
    def __init__(self, owner, balance=0):  # balance는 기본값 0
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):  # 입금
        self.balance += amount
        print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")

    def withdraw(self, amount):  # 출금
        if self.balance >= amount:  # 잔액이 충분한 경우
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")
        else:  # 잔액이 부족한 경우
            print("잔액이 부족합니다!")

    def check_balance(self):  # 잔액 확인
        print(f"{self.owner}님의 현재 잔액: {self.balance}원")

    
# 객체 생성
account1 = BankAccount("철수", 10000)  # 철수의 계좌, 초기 잔액 10000원
account2 = BankAccount("영희")        # 영희의 계좌, 초기 잔액은 기본값 0원

# 동작 수행
account1.deposit(5000)     # 철수 계좌에 5000원 입금
account1.withdraw(3000)    # 철수 계좌에서 3000원 출금
account1.check_balance()   # 철수 잔액 확인

account2.deposit(2000)     # 영희 계좌에 2000원 입금
account2.withdraw(5000)    # 영희 계좌에서 5000원 출금 (잔액 부족)
account2.check_balance()   # 영희 잔액 확인
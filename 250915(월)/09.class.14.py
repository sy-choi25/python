# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __init__
# 메소드
# __str__ __eq__ __ne__ __it__ __gt__ __le__ __ge__
# property->  getter, setter, deleter, private -> 함수를 변수처럼 사용
# 객체 생성

# 상품관리 product
# 상품명 product_name, 가격product_price, 재고product_stock

class Product:
    count = 0
    def __init__(self, product_name, product_price, product_stock):
        self.id = Product.count + 1
        Product.count += 1
        self.product_name = product_name
        self._product_price = product_price
        self._product_stock = product_stock
    @property
    def product_price(self):
        return self._product_price
    @product_price.setter
    def product_price(self, value):
        if value < 0:
            print("가격은 0보다 작을 수 없습니다.")
        else:
            self._product_price = value
    @property
    def product_stock(self):
        return self._product_stock
    @product_stock.setter
    def product_stock(self, value):
        if value < 0:
            print("재고는 0보다 작을 수 없습니다.")
        else:
            self._product_stock = value            

    def __str__(self):
        return f'상품명: {self.product_name}, 가격: {self.product_price}, 재고: {self.product_stock}'
    


product = [
    Product("노트북", 100000,10),
    Product("스마트폰", 200000,20),
    Product("태블릿", 300000,15)
]


# 노트북의 가격을 20% 인하
# 스마트폰은 가격을 10% 인상
# 제품 출력
# 제품 추가
# 제품 삭제 - 수량이 남아 있으면 삭제 못하게
# 현재 모든 제품의 수량의 합
# 가격 x 수량을 기준으로 같다, 크다, 크거나 같다, 작거나 같다


note = product[0]
smart = product[1]
tab = product[2]
# 1.
print(note)
note.product_price = note.product_price*0.8
print(note)

# 2
print(smart)
smart.product_price = (smart.product_price*0.1)+ smart.product_price
print(smart)

# 3.
for p in product:
    print(p)

# 4.
product.append(Product("헤드폰", 50000, 30))

# 5

# 6
# 1)
total_stock = 0
for p in product:
    total_stock += p.product_stock

print("모든 제품의 총 재고:", total_stock)
#2)
total_stock = sum(p.product_stock for p in product)
print("모든 제품의 총 재고:", total_stock)
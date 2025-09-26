# 리스트 컴프리핸션
# 두개 동일한 의미

# 1)
total = []
for i in range(1,11):
    total.append(i)
# 2)
print([ i for i in range(1,11)]) # []에 " i for i in range(1,11)" 을 담겠다

import random
total = []
for i in range(5):
    total.append(random.randint(1,10))

print([random.randint(1,10) for i in range(5)])

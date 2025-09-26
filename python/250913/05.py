# python_score = input("파이썬 점수를 입력하세요")
# java_score = input("자바 점수를 입력하세요")
# c_lan_score = input("씨언어 점수를 입력하세요")
# subject = ["python", "java", "c_lan"]
# scores = [python_score,java_score,c_lan_score ]
# total_dict = dict(zip(subject, scores))


x = ["파이썬", "자바", "C언어"]
y = []
z = {}

for i in range(len(x)):
  y.append(int(input(f"{x[i]} 점수 입력 : ")))
z = dict(zip(x, y))

print()
print("=====성적표=====")

def print_score(x):
  for i, j in x.items():
    print(f"{i} 점수 : {j}점")

def cal_avg(x):
  avg = sum(x.values()) / len(x.items())
  return avg

print_score(z)
print(f"평균점수 : {round(cal_avg(z),2)}점")

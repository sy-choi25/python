from pydantic import BaseModel,Field
class User(BaseModel):
    name : str
    age : int
user = User(name = '홍길동', age = '18')
print(user)
print(user.name)
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name:str
    email:EmailStr
    account_id:int

user_data = {
    'name':"Kaushik",
    'email':"kaushik@gmail.com",
    'account_id': '1234'
}

user = User(**user_data)
print(user)


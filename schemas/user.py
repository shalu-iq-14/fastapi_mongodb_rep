from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    full_name:str
    email:EmailStr
    phone: str
    password: str

class User_Login(BaseModel):
    email:EmailStr
    password: str
from pydantic import BaseModel
from pydantic import EmailStr


class UserInM(BaseModel):
    email: EmailStr
    password: str


class UserOutM(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True

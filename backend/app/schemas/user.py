import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr = None
    nickname: str = None


class UserCreate(UserBase):
    email: EmailStr
    nickname: str
    password: str


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    created_at: datetime.datetime

    class Config:
        orm_mode = True

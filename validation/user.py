from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    phone: str
    name: str
    city: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

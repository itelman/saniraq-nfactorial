from typing import Optional

from pydantic import BaseModel


class ShanyrakBase(BaseModel):
    type: str
    price: float
    address: str
    area: float
    rooms_count: int
    description: str


class ShanyrakCreate(ShanyrakBase):
    pass


class Shanyrak(ShanyrakBase):
    id: int
    owner_id: int
    total_comments: Optional[int] = 0

    class Config:
        orm_mode = True

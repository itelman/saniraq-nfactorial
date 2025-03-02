from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from pkg import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone = Column(String)
    name = Column(String)
    city = Column(String)
    shanyraks = relationship("Shanyrak", back_populates="owner")
    comments = relationship("Comment", back_populates="author")

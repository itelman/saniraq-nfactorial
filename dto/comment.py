from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from pkg import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=func.now())
    author_id = Column(Integer, ForeignKey("users.id"))
    shanyrak_id = Column(Integer, ForeignKey("shanyraks.id"))

    author = relationship("User", back_populates="comments")
    shanyrak = relationship("Shanyrak", back_populates="comments")

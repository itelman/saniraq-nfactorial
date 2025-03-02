from sqlalchemy.orm import Session

from dto import Shanyrak
from validation import ShanyrakCreate, ShanyrakBase


class ShanyrakRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_shanyrak(self, shanyrak: ShanyrakCreate, owner_id: int):
        db_shanyrak = Shanyrak(
            **shanyrak.dict(), owner_id=owner_id
        )
        self.db.add(db_shanyrak)
        self.db.commit()
        self.db.refresh(db_shanyrak)
        return db_shanyrak

    def get_shanyrak(self, shanyrak_id: int):
        return self.db.query(Shanyrak).filter(Shanyrak.id == shanyrak_id).first()

    def update_shanyrak(self, shanyrak_id: int, shanyrak_update: ShanyrakBase):
        db_shanyrak = self.get_shanyrak(shanyrak_id)
        if db_shanyrak:
            for key, value in shanyrak_update.dict(exclude_unset=True).items():
                setattr(db_shanyrak, key, value)
            self.db.commit()
            self.db.refresh(db_shanyrak)
        return db_shanyrak

    def delete_shanyrak(self, shanyrak_id: int):
        db_shanyrak = self.get

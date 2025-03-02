from fastapi import HTTPException
from sqlalchemy.orm import Session

from dto import User, Shanyrak
from repository import ShanyrakRepository, CommentRepository
from validation import ShanyrakCreate, ShanyrakBase, CommentCreate, CommentBase


class ShanyrakService:
    def __init__(self, db: Session):
        self.shanyrak_repo = ShanyrakRepository(db)
        self.comment_repo = CommentRepository(db)

    def create_shanyrak(self, shanyrak: ShanyrakCreate, current_user: User):
        return self.shanyrak_repo.create_shanyrak(shanyrak, current_user.id)

    def get_shanyrak(self, shanyrak_id: int):
        shanyrak = self.shanyrak_repo.get_shanyrak(shanyrak_id)
        if not shanyrak:
            raise HTTPException(status_code=404, detail="Shanyrak not found")
        total_comments = len(shanyrak.comments)
        shanyrak_schema = Shanyrak.from_orm(shanyrak)
        shanyrak_schema.total_comments = total_comments
        return shanyrak_schema

    def update_shanyrak(self, shanyrak_id: int, shanyrak_update: ShanyrakBase, current_user: User):
        shanyrak = self.shanyrak_repo.get_shanyrak(shanyrak_id)
        if not shanyrak:
            raise HTTPException(status_code=404, detail="Shanyrak not found")
        if shanyrak.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        return self.shanyrak_repo.update_shanyrak(shanyrak_id, shanyrak_update)

    def delete_shanyrak(self, shanyrak_id: int, current_user: User):
        shanyrak = self.shanyrak_repo.get_shanyrak(shanyrak_id)
        if not shanyrak:
            raise HTTPException(status_code=404, detail="Shanyrak not found")
        if shanyrak.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        return self.shanyrak_repo.delete_shanyrak(shanyrak_id)

    def create_comment(self, shanyrak_id: int, comment: CommentCreate, current_user: User):
        shanyrak = self.shanyrak_repo.get_shanyrak(shanyrak_id)
        if not shanyrak:
            raise HTTPException(status_code=404, detail="Shanyrak not found")
        return self.comment_repo.create_comment(comment, current_user.id, shanyrak_id)

    def get_comments(self, shanyrak_id: int):
        shanyrak = self.shanyrak_repo.get_shanyrak(shanyrak_id)
        if not shanyrak:
            raise HTTPException(status_code=404, detail="Shanyrak not found")
        return self.comment_repo.get_comments(shanyrak_id)

    def update_comment(self, shanyrak_id: int, comment_id: int, comment_update: CommentBase,
                       current_user: User):
        comment = self.comment_repo.get_comment(comment_id)
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        if comment.author_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        return self.comment_repo.update_comment(comment_id, comment_update)

    def delete_comment(self, shanyrak_id: int, comment_id: int, current_user: User):
        comment = self.comment_repo.get_comment(comment_id)
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        if comment.author_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized")
        return self.comment_repo.delete_comment(comment_id)

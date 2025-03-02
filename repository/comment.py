from sqlalchemy.orm import Session

from dto import Comment
from validation import CommentCreate, CommentBase


class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, comment: CommentCreate, author_id: int, shanyrak_id: int):
        db_comment = Comment(
            **comment.dict(), author_id=author_id, shanyrak_id=shanyrak_id
        )
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment

    def get_comments(self, shanyrak_id: int):
        return self.db.query(Comment).filter(Comment.shanyrak_id == shanyrak_id).all()

    def get_comment(self, comment_id: int):
        return self.db.query(Comment).filter(Comment.id == comment_id).first()

    def update_comment(self, comment_id: int, comment_update: CommentBase):
        db_comment = self.get_comment(comment_id)
        if db_comment:
            for key, value in comment_update.dict(exclude_unset=True).items():
                setattr(db_comment, key, value)
            self.db.commit()
            self.db.refresh(db_comment)
        return db_comment

    def delete_comment(self, comment_id: int):
        db_comment = self.get_comment(comment_id)
        if db_comment:
            self.db.delete(db_comment)
            self.db.commit()
        return db_comment

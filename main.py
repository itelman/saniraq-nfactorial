from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from pkg import get_db
from service import AuthService, ShanyrakService
from service.auth import get_current_user
from validation import User, UserCreate, Token, UserBase, Shanyrak, ShanyrakCreate, ShanyrakBase, CommentCreate, \
    Comment, CommentBase

app = FastAPI()


@app.post("/auth/users/", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService(db).register_user(user)


@app.post("/auth/users/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return AuthService(db).login_user(form_data, db)


@app.get("/auth/users/me", response_model=User)
def get_me(current_user: User = Depends(get_current_user)):
    return AuthService(get_db()).get_me(current_user)


@app.patch("/auth/users/me", response_model=User)
def update_me(user_update: UserBase, current_user: User = Depends(get_current_user),
              db: Session = Depends(get_db)):
    return AuthService(db).update_me(current_user, user_update, db)


@app.post("/shanyraks/", response_model=Shanyrak)
def create_shanyrak(shanyrak: ShanyrakCreate, current_user: User = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    return ShanyrakService(db).create_shanyrak(shanyrak, current_user)


@app.get("/shanyraks/{shanyrak_id}", response_model=Shanyrak)
def get_shanyrak(shanyrak_id: int, db: Session = Depends(get_db)):
    return ShanyrakService(db).get_shanyrak(shanyrak_id)


@app.patch("/shanyraks/{shanyrak_id}", response_model=Shanyrak)
def update_shanyrak(shanyrak_id: int, shanyrak_update: ShanyrakBase,
                    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return ShanyrakService(db).update_shanyrak(shanyrak_id, shanyrak_update, current_user)


@app.delete("/shanyraks/{shanyrak_id}", status_code=status.HTTP_200_OK)
def delete_shanyrak(shanyrak_id: int, current_user: User = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    return ShanyrakService(db).delete_shanyrak(shanyrak_id, current_user)


@app.post("/shanyraks/{shanyrak_id}/comments", status_code=status.HTTP_200_OK, response_model=Comment)
def create_comment(shanyrak_id: int, comment: CommentCreate,
                   current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return ShanyrakService(db).create_comment(shanyrak_id, comment, current_user)


@app.get("/shanyraks/{shanyrak_id}/comments", response_model=list[Comment])
def get_comments(shanyrak_id: int, db: Session = Depends(get_db)):
    return ShanyrakService(db).get_comments(shanyrak_id)


@app.patch("/shanyraks/{shanyrak_id}/comments/{comment_id}", status_code=status.HTTP_200_OK,
           response_model=Comment)
def update_comment(shanyrak_id: int, comment_id: int, comment_update: CommentBase,
                   current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return ShanyrakService(db).update_comment(shanyrak_id, comment_id, comment_update, current_user)


@app.delete("/shanyraks/{shanyrak_id}/comments/{comment_id}", status_code=status.HTTP_200_OK)
def delete_comment(shanyrak_id: int, comment_id: int, current_user: User = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    return ShanyrakService(db).delete_comment(shanyrak_id, comment_id, current_user)

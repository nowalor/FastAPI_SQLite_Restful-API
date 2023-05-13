from fastapi import Depends
from main import app, get_db
import models
from sqlalchemy.orm import Session
import schemas
from helpers.hasher import Hasher
from pydantic import BaseModel


class LoginPayload(BaseModel):
    password: str
    email: str


@app.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    user_model = models.User()

    user_model.email = user.email
    user_model.password = Hasher.generate_hash(user.password)

    db.add(user_model)
    db.commit()


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.post("/login")
def login(login_info: LoginPayload, db: Session = Depends(get_db)):
    email = login_info.email
    password = login_info.password

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        return "No user!"

    if not Hasher.verify_hash(password, user.password):
        return "not a match"

    return "hash matches"

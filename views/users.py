from fastapi import Depends
from main import app, get_db
import models
from sqlalchemy.orm import Session
import schemas


@app.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    user_model = models.User()

    user_model.email = user.email
    user_model.password = user.password

    db.add(user_model)
    db.commit()

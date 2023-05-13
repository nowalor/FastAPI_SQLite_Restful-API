from fastapi import FastAPI, Depends
import uvicorn
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
from pydantic import BaseModel

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class User(BaseModel):
    email: str
    password: str


class Note(BaseModel):
    user_id: int
    text: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    except:
        print("Some exception")
    finally:
        db.close()


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Note).all()


@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    user_model = models.User()

    user_model.email = user.email
    user_model.password = user.password

    db.add(user_model)
    db.commit()


@app.post("/notes")
def create_note(note: Note, db: Session = Depends(get_db)):
    note_model = models.Note()

    note_model.user_id = note.user_id
    note_model.text = note.text

    db.add(note_model)
    db.commit()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

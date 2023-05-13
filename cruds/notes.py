from fastapi import Depends
from main import app, get_db
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas


@app.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()


@app.post("/notes")
def create_note(note: schemas.Note, db: Session = Depends(get_db)):
    note_model = models.Note()

    note_model.user_id = note.user_id
    note_model.text = note.text

    db.add(note_model)
    db.commit()

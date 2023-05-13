from fastapi import FastAPI, Depends
import uvicorn
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    except:
        print("Some exception")
    finally:
        db.close()


# All Views
import views.notes
import views.users


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

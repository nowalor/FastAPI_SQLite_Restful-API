from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


class Note(BaseModel):
    user_id: int
    text: str

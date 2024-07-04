from pydantic import BaseModel


class User(BaseModel):
    password: str
    name: str
    bio: str


class Book(BaseModel):
    name: str
    description: str
    author: int
    paid: bool
    visibility: bool


class Author(BaseModel):
    name: str

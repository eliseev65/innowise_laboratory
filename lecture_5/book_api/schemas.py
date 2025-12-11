from pydantic import BaseModel
from typing import Optional

# Pydantic models for Book API

class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class BookFilter(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True
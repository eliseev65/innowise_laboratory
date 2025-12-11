from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate, BookUpdate

# CRUD operations for Book model

def apply_substring_filter(query, column, value: str):
    for part in value.split():
        query = query.filter(column.ilike(f"%{part}%"))
    return query

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author,
        year=book.year
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return True
    return False


def update_book(db: Session, book_id: int, data: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    
    if data.title is not None:
        book.title = data.title
    if data.author is not None:
        book.author = data.author
    if data.year is not None:
        book.year = data.year
    
    db.commit()
    db.refresh(book)
    return book


def search_books(db: Session, title: str | None, author: str | None, year: int | None):
    query = db.query(Book)

    if title:
        query = apply_substring_filter(query, Book.title, title)
    if author:
        query = apply_substring_filter(query, Book.author, author)
    if year:
        query = query.filter(Book.year == year)

    return query.all()
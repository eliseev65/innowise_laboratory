from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import crud
from schemas import BookRead, BookCreate, BookUpdate, BookFilter

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ========== Endpoints ==========
@app.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.get("/books/", response_model=list[BookRead])
def read_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return crud.get_books(db, skip=skip, limit=limit)


@app.get("/books/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"status": "deleted"}


@app.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/books/search/", response_model=list[BookRead])
def search_books(
    filters: BookFilter = Depends(),

    db: Session = Depends(get_db)
):
    return crud.search_books(db, filters.title, filters.author, filters.year)
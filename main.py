from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from database import engine, SessionLocal

# Ye line PostgreSQL me "books" table bana deti hai
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Har request ke liye DB ka session kholna aur kaam ke baad band karna
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1) CREATE - nayi book add
@app.post("/books")
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(title=book.title, author=book.author, available=book.available)
    db.add(new_book)       # book ko add karo
    db.commit()            # save karo
    db.refresh(new_book)   # id wapas lo
    return new_book


# 2) READ - saari books dekho
@app.get("/books", response_model=list[schemas.BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


# 3) READ - ek book dekho
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# 4) UPDATE - book change karo
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, data: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = data.title
    book.author = data.author
    book.available = data.available
    db.commit()
    db.refresh(book)
    return book


# 5) DELETE - book hatao
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}
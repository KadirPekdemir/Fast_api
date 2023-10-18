from fastapi import FastAPI
from typing import List
from . import models, database

app = FastAPI()

# Database initialization
database.Base.metadata.create_all(bind=database.engine)

# CRUD operations for books
@app.post("/books/")
def create_book(book: models.Book):
    db = database.SessionLocal()
    db.add(book)
    db.commit()
    db.refresh(book)
    db.close()
    return book

@app.get("/books/")
def read_books(skip: int = 0, limit: int = 10):
    db = database.SessionLocal()
    books = db.query(models.Book).offset(skip).limit(limit).all()
    db.close()
    return books

# CRUD operations for patrons
@app.post("/patrons/")
def create_patron(patron: models.Patron):
    db = database.SessionLocal()
    db.add(patron)
    db.commit()
    db.refresh(patron)
    db.close()
    return patron

@app.get("/patrons/")
def read_patrons(skip: int = 0, limit: int = 10):
    db = database.SessionLocal()
    patrons = db.query(models.Patron).offset(skip).limit(limit).all()
    db.close()
    return patrons

# Checkout and return books by patrons
@app.post("/checkout/{book_id}/{patron_id}/")
def checkout_book(book_id: int, patron_id: int):
    db = database.SessionLocal()
    # Implement checkout logic here
    db.close()
    return {"message": "Book checked out successfully."}

@app.post("/return/{book_id}/{patron_id}/")
def return_book(book_id: int, patron_id: int):
    db = database.SessionLocal()
    # Implement return logic here
    db.close()
    return {"message": "Book returned successfully."}

# List all checked-out books
@app.get("/checked-out/")
def list_checked_out_books():
    db = database.SessionLocal()
    # Implement logic to list checked-out books here
    db.close()
    return []

# List all overdue books
@app.get("/overdue/")
def list_overdue_books():
    db = database.SessionLocal()
    # Implement logic to list overdue books here
    db.close()
    return []

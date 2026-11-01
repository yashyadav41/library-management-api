# Library Management API

Simple CRUD API built with FastAPI, SQLAlchemy and PostgreSQL.

## Features
- Add a book
- View all books / one book
- Update a book
- Delete a book

## Setup
1. Install PostgreSQL and create a database named `library_db`
2. Create a virtual environment and activate it
3. Run: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and put your PostgreSQL password
5. Run: `uvicorn main:app --reload`
6. Open: http://127.0.0.1:8000/docs

## API Endpoints
| Method | URL | Description |
|---|---|---|
| POST | /books | Add a book |
| GET | /books | List all books |
| GET | /books/{id} | Get one book |
| PUT | /books/{id} | Update a book |
| DELETE | /books/{id} | Delete a book |
# JA Vocab API Demo (FastAPI + PostgreSQL + JWT)

A portfolio project showing FastAPI CRUD APIs with JWT-protected writes and public reads.

## Features

- JWT demo token (`/demo_token`)
- Public GETs (`/words`, `/words/{id}`)
- Authenticated POST/PUT/DELETE
- Search, filters, error handling

## Setup

1. Clone repo
2. Create virtualenv
3. Install requirements:

pip install -r requirements.txt

Create .env file with:

SECRET_KEY=your_secret
DATABASE_URL=postgresql://user:pass@localhost:5432/ja_vocab
ACCESS_TOKEN_EXPIRE_MINUTES=30

Run server:
uvicorn main:app --reload

Tests
pytest -v

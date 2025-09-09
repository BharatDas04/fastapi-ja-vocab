from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.vocab_database import BASE
import os

uri: str = os.getenv("DATABASE_URL")

engine = create_engine(uri,
    pool_pre_ping=True,
    pool_recycle=1800,)
BASE.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.vocab_database import BASE
import os

uri: str = os.getenv("DATABASE_URL")

engine = create_engine(uri,
    pool_pre_ping=True,
    pool_recycle=1800,)
BASE.metadata.create_all(bind=engine)

session = sessionmaker(
    bind=engine,
    autoflush = True,
)

db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print("DB conncected")

except Exception as e:
    print(f'Error: {str(e)}')

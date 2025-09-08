from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, func, Sequence, Enum
import random

def generate_random_id():
    return random.randint(1000, 1999)

BASE = declarative_base()
LEVELS = ("N5", "N4", "N3", "N2", "N1")

class Vocab(BASE):
    __tablename__ = "vocab_list"
    vocab_id = Column(Integer, Sequence("vocab_id_seq", start=1000), primary_key = True)
    surface = Column(String(120), nullable=False)
    reading = Column(String(200), nullable=True)
    meaning = Column(String(240), nullable=False)
    jlpt_level = Column(Enum(*LEVELS, name="level_enum", native_enum=False), nullable=False, default="N1")
    owner_hint = Column(String(50))
    added_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

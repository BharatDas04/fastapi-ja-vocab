from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import datetime


class JLPTLEVELS(str, Enum):
    N5 = "N5"
    N4 = "N4"
    N3 = "N3"
    N2 = "N2"
    N1 = "N1"

class createVocab(BaseModel):
    surface: str = Field(..., min_length=1, max_length=120)
    reading: Optional[str] = Field(None, min_length=1, max_length=200)
    meaning: str = Field(..., min_length=1, max_length=240)
    jlpt_level: JLPTLEVELS = JLPTLEVELS.N1
    
class demoToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int

class WordAdded(BaseModel):
    status: str
    vocab_id: int

class wordResponse(BaseModel):
    meaning: str
    vocab_id: int
    owner_hint: str
    added_at: datetime
    jlpt_level: JLPTLEVELS
    surface: str
    reading: str
    updated_at: datetime

class editVocab(BaseModel):
    vocab_id: int
    surface: str | None = Field(..., min_length=1, max_length=120)
    reading: Optional[str] | None = Field(None, min_length=1, max_length=200)
    meaning: str  | None= Field(..., min_length=1, max_length=240)
    jlpt_level: JLPTLEVELS | None = JLPTLEVELS.N1
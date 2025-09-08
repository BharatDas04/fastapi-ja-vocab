import sys
sys.path.append("./")
from connection import db_session
from Model.vocab_database import Vocab
from Schemas.schemas import createVocab, editVocab
from typing import Optional
from sqlalchemy import or_

def create_vocab(word: createVocab):
    try:
        obj = word.model_dump()
        obj["owner_hint"] = "demo"
        
        # Validating if "word exists or not"
        
        existing = ( db_session.query(Vocab).filter(
            Vocab.surface == obj["surface"],
            Vocab.meaning == obj["meaning"],
            Vocab.reading == obj.get("reading"),
        ).first() )

        if existing:
            return None
        
        data = Vocab(**obj)    
        db_session.add(data)
        db_session.commit()

        return {"status": "OK", "vocab_id": data.vocab_id}
    
    except Exception as e:
        return {"status": "Error", "message": str(e)} 

def get_word(vocab_id: int):
    try:
        res = db_session.query(Vocab).filter(
            Vocab.vocab_id == vocab_id,
        ).first()
        return res

    except Exception as e:
        return {
            "status":"Error",
            "message": str(e)
        }
    
def search_word(q: Optional[str] = None):
    try:
        query = db_session.query(Vocab)
        
        # if a search query is present
        if q:
            like = f"%{q}%"
            query = query.filter(
                or_(
                    Vocab.surface.ilike(like),
                    Vocab.meaning.ilike(like),
                    Vocab.reading.ilike(like),
                )
            )
            return query.all()

        # if not present then return 10 recently added words
        res = db_session.query(Vocab).order_by(Vocab.added_at.desc()).limit(10).all()
        db_session.commit()
        return res

    except Exception as e:
        return {
            "status":"Error",
            "message": str(e)
        }
    
def delete_word(vocab_id: int):
    try:
        res = db_session.query(Vocab).filter(Vocab.vocab_id == vocab_id).first()
        print(res)
        if res is None:
            return False
        res = db_session.delete(res)
        db_session.commit()
        return True
    
    except Exception as e:
        return {
            "status":"Error",
            "message": str(e)
        }

def word_edit(doc: editVocab):
    try:
        data = doc.model_dump()
        query = db_session.query(Vocab).filter(Vocab.vocab_id == data['vocab_id']).first()
        if not query:
            return None
        for key, val in data.items():
            setattr(query, key, val)
        
        db_session.commit()
        db_session.refresh(query) 
        return query
    
    except Exception as e:
        return {
            "status":"Error",
            "message": str(e)
        }
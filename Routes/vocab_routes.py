from fastapi import APIRouter
from DBOperations import operations as op
from Schemas.schemas import createVocab, demoToken, WordAdded, wordResponse, editVocab
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from Auth.auth import create_demo_token ,verify_token
from typing import List

security = HTTPBearer()
    
vocab_route = APIRouter()

def require_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    return True

@vocab_route.get("/")
def root():
    return {"status": "ok"}

@vocab_route.get("/healthz")
def check_health():
    return {"status": "ok"}

@vocab_route.post("/demo_token", response_model = demoToken)
def demo_token():
    token = create_demo_token()
    return {"access_token": token, "token_type": "bearer", "expires_in_minutes": 30}

@vocab_route.post("/word", dependencies=[Depends(require_token)], response_model = WordAdded)
def add_word(word: createVocab):
    res = op.create_vocab(word)
    if res is None:
        raise HTTPException(status_code=409, detail="Word already exists")
    return res

@vocab_route.get("/words/{vocab_id}", response_model = wordResponse)
def read_words(vocab_id: int):
    res = op.get_word(vocab_id)
    if res is None:
        raise HTTPException(status_code=404, detail=f'No word with id: {vocab_id}')
    return res

@vocab_route.get("/words", response_model = List[wordResponse])
def list_words(q: str | None = None):
    return op.search_word(q)

@vocab_route.delete("/words/{vocab_id}", dependencies=[Depends(require_token)])
def delete_word(vocab_id: int):
    res = op.delete_word(vocab_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"No word found with id {vocab_id}")
    return {
        "status": "ok",
        "message": "Deleted"
    }

@vocab_route.put("/words" , dependencies=[Depends(require_token)])
def edit_word(doc: editVocab):
    res = op.word_edit(doc)
    if not res:
        raise HTTPException(status_code=400, detail="Wrong Input")
    return res

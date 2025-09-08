from fastapi import FastAPI
from Routes.vocab_routes import vocab_route
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="JA Vocab Tracker",
    description="Public read; JWT-protected writes. Swagger UI available at /docs.",
    version="0.1.0",
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=False,
    allow_methods=["*"],   
    allow_headers=["*"],  
)

app.include_router(vocab_route)
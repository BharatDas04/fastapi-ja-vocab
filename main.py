from fastapi import FastAPI
from Routes.vocab_routes import vocab_route

app = FastAPI(
    title="JA Vocab Tracker",
    description="Public read; JWT-protected writes. Swagger UI available at /docs.",
    version="0.1.0",
    )

app.include_router(vocab_route)
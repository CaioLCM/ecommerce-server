from fastapi import FastAPI
from .routes.user import user_router
from contextlib import asynccontextmanager
from .database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_route():
    return {"status": "ok!"}

app.include_router(user_router)

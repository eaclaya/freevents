from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.events import router as events_router
from src.api.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    init_db()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(events_router, prefix="/api/events")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
def read_api_health():
    return {"status": "ok"}
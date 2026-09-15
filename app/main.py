from fastapi import FastAPI
from sqlalchemy import text

from .session import SessionDep

app = FastAPI()


@app.get("/health")
async def health(session: SessionDep) -> dict[str, str]:
    await session.execute(text("SELECT 1"))
    return {"health": "ok"}


@app.post("/ask")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

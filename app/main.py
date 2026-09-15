from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

from fastapi import FastAPI

app = FastAPI()


@app.post("/ask")
def read_root():
    return {"Hello": "World"}
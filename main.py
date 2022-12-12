
from fastapi import FastAPI
from uuid import UUID


app = FastAPI()

@app.get("/documents/{document_id}")
async def read_item(
        document_id: UUID):
    return {"document_id": document_id}
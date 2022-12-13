"""Main entry point."""
from uuid import UUID

from fastapi import FastAPI

from db import database, get_document, create_document


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/documents/{document_id}")
async def read_document(
        document_id: UUID):
    return await get_document(document_id)


@app.post("/documents/")
async def create_read_document():
    document = await create_document()
    return document

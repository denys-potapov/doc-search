"""Main entry point."""
from uuid import UUID

from fastapi import FastAPI, File, BackgroundTasks
from fastapi.concurrency import run_in_threadpool

from ocr import get_text
import db


app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.database.disconnect()


async def process_document(document_id, stream: bytes):
    """Processs uploaded document."""
    text = await run_in_threadpool(lambda: get_text(stream))
    await db.update_document_text(document_id, text)


@app.get("/documents/{document_id}")
async def get_document(
        document_id: UUID):
    return await db.get_document(document_id)


@app.post("/documents/")
async def create_document(
        background_tasks: BackgroundTasks,
        file: bytes = File()):
    document = await db.create_empty_document()
    background_tasks.add_task(process_document, document["id"], file)

    return document

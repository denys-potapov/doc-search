"""DB related."""
import re

import databases

DATABASE_URL = "postgresql://postgres:1@localhost/documents"

database = databases.Database(DATABASE_URL)


async def get_document(id):
    """Get document by id."""
    query = "SELECT * FROM documents WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": id})


async def create_empty_document():
    """Create new document."""
    query = "INSERT INTO documents DEFAULT VALUES RETURNING *"
    return await database.fetch_one(query=query)


async def update_document_text(id, text):
    """Update document text and status."""
    query = """
        UPDATE documents
        SET
            text = :text,
            status = :status
        WHERE
            id = :id
    """
    values = {
        "id": id,
        "text": text,
        "status": "OK"
    }
    return await database.execute(query=query, values=values)


def plainto_tsquery(query):
    """Convert plain query to tsquery input.
    Supports ! (not) and * (prefix) modifiers."""
    words = re.findall(r'!?\w+\*?', query)
    return " & ".join(words).replace('*', ':*')


async def search_documents(plain_query):
    """Search documents."""
    query = """
        SELECT *
        FROM documents
        WHERE
            ts @@ plainto_tsquery('simple', :plain_query)"""

    return await database.fetch_all(
        query=query, values={"plain_query": plain_query})

"""DB related."""
import databases

DATABASE_URL = "postgresql://postgres:1@localhost/documents"

database = databases.Database(DATABASE_URL)


async def get_document(id):
    """Get document by id."""
    query = "SELECT * FROM documents WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": id})

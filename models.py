"""Models."""
from uuid import UUID

from pydantic import BaseModel


class Document(BaseModel):
    id: UUID
    status: str = "PENDING"
    text: str = ''

from pydantic import BaseModel

class Annotation(BaseModel):
    publication_type: str
    publication_id: int
    page: int
    text: str | None = None

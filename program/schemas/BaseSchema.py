from pydantic import BaseModel

class BaseSchema(BaseModel):
    title: str
    author: str | None = None
    year: int
    pages_number: int
    avaliation: int | None = None
    genre: str

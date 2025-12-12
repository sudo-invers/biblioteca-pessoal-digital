from datetime import date
from pydantic import BaseModel

class BaseSchema(BaseModel):
    title: str
    author: str | None = None
    year: int | None = None
    pages_number: int | None = None
    inclusion_date: date | None = None
    genre: str | None = None
    avaliation: int | None = None

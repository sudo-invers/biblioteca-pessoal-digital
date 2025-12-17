from program.domain.PublicationType import PublicationType
from program.schemas.BaseSchema import BaseSchema


class Book(BaseSchema):
    type_: PublicationType = PublicationType.BOOK

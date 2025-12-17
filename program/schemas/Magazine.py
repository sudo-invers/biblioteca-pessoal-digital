from program.domain.PublicationType import PublicationType
from program.schemas.BaseSchema import BaseSchema


class Magazine(BaseSchema):
    edition: int | None = None
    type_: PublicationType = PublicationType.MAGAZINE


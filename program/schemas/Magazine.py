from program.domain.PublicationType import PublicationType
from program.schemas.BaseSchema import BaseSchema


class Magazine(BaseSchema):
    type_: PublicationType = PublicationType.MAGAZINE

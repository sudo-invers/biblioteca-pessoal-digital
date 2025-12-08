from sqlalchemy import Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Magazine(Publication):

    __tablename__ = "magazines"

    edition: Mapped[int] = mapped_column(Integer)

    type_: Mapped[PublicationType] = mapped_column(
        "type",
        Enum(PublicationType),
        default=PublicationType.MAGAZINE
    )
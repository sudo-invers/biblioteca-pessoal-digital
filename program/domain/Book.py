from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Book(Publication):

    __tablename__ = "books"

    type_: Mapped[PublicationType] = mapped_column(
        "type",
        Enum(PublicationType),
        default=PublicationType.BOOK
    )
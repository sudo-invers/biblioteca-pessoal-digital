from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Book(Publication):

    __tablename__ = "book"

    id: Mapped[int] = mapped_column(ForeignKey("publications.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": PublicationType.BOOK
    }

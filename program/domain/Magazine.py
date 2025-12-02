from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Magazine(Publication):

    __tablename__ = "magazine"

    id: Mapped[int] = mapped_column(ForeignKey("publication.id"), primary_key=True)

    edition: Mapped[int] = mapped_column(Integer)

    __mapper_args__ = {
        "polymorphic_identity": PublicationType.MAGAZINE
    }

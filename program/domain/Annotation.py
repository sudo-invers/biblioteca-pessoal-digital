"""
from datetime import date
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from program.domain.Base import Base

class Annotation(Base):
    """
    Represents a anotaion made in a publication
    """

    __tablename__ = "annotations"

    #def __init__(self, text: str, page: int, created_at: datetime):
    #    self.text = text
    #    self.page = page
    #    self.created_at = created_at

    # SqlAlchemy make a init based how the atributes bellow, test it later, and remove in the next 'entrega'

    id: Mapped[int] = mapped_column(primary_key=True)
    # FK for Publication
    publication_id: Mapped[int] = mapped_column(
        ForeignKey("publications.id"),
        nullable=False
    )
    # relacionamento inverso
    publication: Mapped["Publication"] = relationship(  # noqa: F821 # The sqlalchemy injects in the mapping fase
        back_populates="annotations"
    )

    text: Mapped[str] = mapped_column(String)
    page: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[date] = mapped_column(
        Date,
        default=date.today,
        nullable=False
    )

    def __repr__(self):
        return f"<Annotation id={self.id} page={self.page} text={self.text}>"
"""
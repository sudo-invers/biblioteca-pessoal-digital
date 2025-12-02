from datetime import date
from sqlalchemy import BIGINT, Integer, String, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Base import Base
from program.domain.PublicationType import PublicationType
class Publication(Base):
    """
    class that implements Book.py and Magazine.py
    """

    __abstract__ = True

    #sqlAlchemy make the init itself
    
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=True)
    year: Mapped[int] = mapped_column(Integer)
    inclusion_date: Mapped[date] = mapped_column(Date, default=date.today)
    pages_number: Mapped[int] = mapped_column(Integer, nullable=False) # I think i can automatize it later
    avaliation: Mapped[int] = mapped_column(Integer)
    genre: Mapped[str] = mapped_column(String)

    type_: Mapped[PublicationType] = mapped_column(
        Enum(PublicationType),
        nullable=False
    )

    """annotations: Mapped[list["Annotation"]] = relationship( # noqa: F821 # The sqlalchemy injects in the mapping fase
    back_populates="publication",
    cascade="all, delete-orphan"
)"""
 
    __mapper_args__ = {
        "polymorphic_on": "type_",
        "polymorphic_identity": "publication",
        "with_polymorphic": "*"
}

    def synopsis(self):
         return f"Title: {self.title}, author: {self.author}, {self.pages_number} pages"

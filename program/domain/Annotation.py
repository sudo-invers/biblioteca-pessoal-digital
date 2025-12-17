from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Base import Base


class Annotation(Base):
    __tablename__ = "annotations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    publication_type: Mapped[str] = mapped_column(String, nullable=False)
    publication_id: Mapped[int] = mapped_column(Integer, nullable=False)

    page: Mapped[int] = mapped_column(Integer, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[date] = mapped_column(Date, default=date.today)

    def __repr__(self):
        return (
            f"<Annotation id={self.id}"
            f"type={self.publication_type}"
            f"pub_id={self.publication_id}"
            f"page={self.page}>"
        )

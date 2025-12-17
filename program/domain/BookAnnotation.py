from datetime import date
from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from program.domain.Base import Base


class BookAnnotation(Base):
    __tablename__ = "book_annotations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"), nullable=False
    )

    page: Mapped[int] = mapped_column(Integer, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)

    # relationship
    book = relationship("book", back_populates="annotations")

    def __repr__(self):
        return f"<bookAnnotation book_id={self.book_id} page={self.page}>"

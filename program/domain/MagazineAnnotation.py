from datetime import date
from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from program.domain.Base import Base


class MagazineAnnotation(Base):
    __tablename__ = "magazine_annotations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    magazine_id: Mapped[int] = mapped_column(
        ForeignKey("magazines.id", ondelete="CASCADE"), nullable=False
    )

    page: Mapped[int] = mapped_column(Integer, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)

    # relationship
    magazine = relationship("magazine", back_populates="annotations")

    def __repr__(self):
        return f"<MagazineAnnotation magazine_id={self.magazine_id} page={self.page}>"

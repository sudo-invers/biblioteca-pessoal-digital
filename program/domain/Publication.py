from datetime import date
from sqlalchemy import BIGINT, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.Base import Base
class Publication(Base):
    """
    class that implements Book.py and Magazine.py
    """

    __abstract__ = True

    #sqlAlchemy make the init itself
    
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=True)
    year: Mapped[int] = mapped_column(Integer)
    inclusion_date: Mapped[date] = mapped_column(Date, default=date.today)
    pages_number: Mapped[int] = mapped_column(Integer, nullable=True) # I think i can automatize it later
    avaliation: Mapped[int] = mapped_column(Integer)
    genre: Mapped[str] = mapped_column(String)

    def synopsis(self):
         return f"Title: {self.title}, author: {self.author}, {self.pages_number} pages"

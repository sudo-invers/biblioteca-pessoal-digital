from datetime import date
from sqlalchemy import Enum, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from program.domain.AlterStatus import AlterStatus
from program.domain.Base import Base
class Publication(Base):
    """
    class that implements Book.py and Magazine.py
    """

    __abstract__ = True

    #sqlAlchemy make the init itself
    
    #BigInt can't have autoIncrement, switched to Integer

    #sqlite_autoincrement=True
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    inclusion_date: Mapped[date] = mapped_column(Date, default=date.today)   
    pages_number: Mapped[int] = mapped_column(Integer, default=0) # I think i can automatize it later
    avaliation: Mapped[int] = mapped_column(Integer, nullable=True, default=None)
    genre: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[AlterStatus] = mapped_column(Enum(AlterStatus), default=AlterStatus.UNREAD
    )

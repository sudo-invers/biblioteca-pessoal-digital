from sqlalchemy import BigInteger, Column, Date, Enum, Integer, String, func
from sqlalchemy.orm import relationship

from program.domain.Base import Base
from program.domain.PublicationType import PublicationType
class Publication(Base):
    """
    class that implements Book.py and Magazine.py
    """

    __tablename__ = "publications"
    __abstract__ = False

    id = Column(BigInteger, primary_key=True, index=True)
    annotations = relationship("Annotation", back_populates="publication", cascade="all, delete-orphan")

    #sqlAlchemy make the init itself
    title = Column(String, nullable=False)
    author = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    inclusion_date = Column(Date, default=func.current_date, nullable=False) # Defined automaticaly
    pages_number = Column(Integer, nullable=False) # I think i can automatically calculate the page quantity
    avaliation = Column(Integer, nullable=True)
    genre = Column(String, nullable=True) #Maybe a enum later?
    type_ = Column("type",Enum(PublicationType), nullable=False) # Named type_, to not be confused with type(class)

    __mapper_args__ = {
        "polymorphic_identity": "publication",
        "polymorphic_on": type_
}

    def synopsis(self):
         return f"Title: {self.title}, author: {self.author}, {self.pages_number} pages"

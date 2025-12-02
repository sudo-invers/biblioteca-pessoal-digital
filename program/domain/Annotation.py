from datetime import datetime

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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

    id = Column(Integer, primary_key=True)
    publication_id = Column(Integer, ForeignKey("publications.id"))
    publication = relationship("Publication", back_populates="annotations")

    text = Column(String, nullable=True) # I can just mark the page if i want
    page = Column(Integer, nullable=False)
    created_at = Column(Date, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Annotation id={self.id} page={self.page} text={self.text[:255]}>"

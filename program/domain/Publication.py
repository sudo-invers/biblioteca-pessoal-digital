from abc import ABC
from sqlite3 import Date
import string

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from program.domain import Anotation, PublicationType, ReadingStatus

Base = declarative_base()

class Publication(Base):
    """
    classe que ira vai ser implementada em Livro.py e Revista.py
    """
    
    __tablename__ = "publications"
    __abstract__ = False

    id = Column(Integer, primarykey=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(String, nullable=False)
    inclusiondate = Column(String, nullable=False)
    pagesnumber = Column(String, nullable=False)
    avaliation = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    anotations = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def init(self, id: int, title: string, author: string, year: int, inclusionDate: Date, pagesNumber: int, avaliation: int, genre: string, anotations: Anotation.Anotation, status: ReadingStatus, type: PublicationType):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.inclusionDate = inclusionDate
        self.pagesNumber = pagesNumber
        self.avaliation = avaliation
        self.genre = genre
        self.anotations = anotations
        self.status = status
        self.type = type
    
    def synopsis(self):
         return f"Title: {self.title}, author: {self.author}, {self.pagesNumber} pages"

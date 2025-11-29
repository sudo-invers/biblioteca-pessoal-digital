from sqlalchemy import Column, Integer
from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Book(Publication):

    __mapper_args__ = {
        "polymorphic_identity": "book"
    }

    edition = Column(Integer)

    def __init__(self, id, title, author, year, inclusionDate, pagesNumber, avaliation, genre, anotations, status):
        super().__init__(id, title, author, year, 
                        inclusionDate, pagesNumber, avaliation,
                        genre, anotations, status, type=PublicationType.BOOK)
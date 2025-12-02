from sqlalchemy import Column, Integer
from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Magazine(Publication):

    __mapper_args__ = {
        "polymorphic_identity": "magazine"
    }

    edition = Column(Integer)

    def __init__(self, id, title, author, year, inclusionDate, pagesNumber, avaliation, genre, anotations, status, edition):
        super().__init__(id, title, author,
                        year, inclusionDate, pagesNumber,
                        avaliation, genre, anotations,
                        status, edition, type_=PublicationType.MAGAZINE)

        self._edition = edition
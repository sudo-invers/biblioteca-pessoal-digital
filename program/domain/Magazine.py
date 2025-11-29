from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Magazine(Publication):
    def __init__(self, id, title, author, year, inclusionDate, pagesNumber, avaliation, genre, anotations, status, edition):
        super().__init__(id, title, author,
                        year, inclusionDate, pagesNumber,
                        avaliation, genre, anotations,
                        status, edition, type=PublicationType.MAGAZINE)

        self._edition = edition
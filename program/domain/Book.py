from program.domain.Publication import Publication
from program.domain.PublicationType import PublicationType

class Book(Publication):
    def __init__(self, id, title, author, year, inclusionDate, pagesNumber, avaliation, genre, anotations, status):
        super().__init__(id, title, author, year, 
                        inclusionDate, pagesNumber, avaliation,
                        genre, anotations, status, type=PublicationType.BOOK)
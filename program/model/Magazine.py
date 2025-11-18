from program.model import Obra

class Revista(Obra):
    def __init__(self, id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation, page_number, edition):
        super().__init__(id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation, page_number)

        self._edition = edition

    
    
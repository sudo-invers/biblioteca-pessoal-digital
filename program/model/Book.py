from program.model import Obra

class Livro(Obra):
    def __init__(self, id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation, page_number):
        super().__init__(id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation, page_number)
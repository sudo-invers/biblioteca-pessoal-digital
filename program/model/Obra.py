from abc import ABC

@property
class Obra(ABC):
    """
    classe que ira vai ser implementada em Livro.py e Revista.py
    """

    def __init__(self, id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation):
        self._id             = id
        self._title          = title
        self._author         = author
        self._year           = year
        self._type           = type      # [livro ou revista]
        self.genre           = genre
        self._pages_quantity = pages_quantity
        self._status         = status    # [naoLido, lido, lendo]
        self._avaliation     = avaliation # [0 _ 10(opcional)]
        self._anotation      = anotation# [data e trecho]
    
    def sinopse(self):
        return f"Title: {self._title} - Author {self._author} - {self._pages_quantity} pages"


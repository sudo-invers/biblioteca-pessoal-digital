from abc import ABC
from sqlite3 import Date
import string

from program.domain import Anotation, PublicationType, ReadingStatus

@property
class Publication(ABC):
    """
    classe que ira vai ser implementada em Livro.py e Revista.py
    """

    def __init__(self, id: int, title: string, author: string, year: int, inclusionDate: Date, pagesNumber: int, avaliation: int, genre: string, anotations: Anotation.Anotation, status: ReadingStatus, type: PublicationType):
        self._id = id
        self._title = title
        self._author = author
        self._year = year
        self._inclusionDate = inclusionDate
        self._pagesNumber = pagesNumber
        self._avaliation = avaliation
        self._genre = genre
        self._anotations = anotations
        self._status = status
        self._type = type
    
    def synopsis(self):
         return f"Title: {self._title}, author: {self._author}, {self._pagesNumber} pages"

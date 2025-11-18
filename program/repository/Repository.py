from abc import ABC
from sqlite3 import Date
import string

from program.repository.RepositoryConnection import RepositoryConnection as execute

# isso, vai dar sql injection com 100% de certeza;
@property
class Repository(ABC):
    """
    Repositorio base que sera vai extendido nos outros repositorios criados
    """

    def __init__(self, execute, query:string):
        self._query = query
        self._execute = execute

    def save(query, name_class, title, author, year, type, genre, pages_quantity, status, avaliation, anotation):

        """
        Docstring for save
        
        :param name_class: Use os nomes que estão em program.model apenas;
        """

        query = """
                INSERT INTO ? (title, author, year, type, genre, pages_quantity, status, avaliation, anotation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                """, name_class, title, author, year, type, genre, pages_quantity, status, avaliation, anotation
        return query
    def getAll():
        pass
    def getById(id:int):
        pass
    def findByTitle(title:string): 
        pass
    def findByAuthor(author:string): 
        pass
    def findByGenre(genre:string): 
        pass
    def findByStatus(status:string): 
        pass
    #def findByReadingPeriod(period:Date): 
        pass
    def deleteById(id:int): 
        pass

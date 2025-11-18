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
        return query
    def getById(id:int):
        return query
    def findByTitle(title:string): 
        return query
    def findByAuthor(author:string): 
        return query
    def findByGenre(genre:string): 
        return query
    def findByStatus(status:string): 
        return query
    #def findByReadingPeriod(period:Date): 
        #return query
    def deleteById(id:int): 
        return query

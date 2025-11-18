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

    def save(titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao):
        query = """
                INSERT INTO Obra (titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                """, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao 
        return execute(query)
    
    def getAll():
        """
        Docstring para getAll
        
        :return: Returns all the info from the bookshelf.db (query for debug only)
        :rtype: Literal['select * from bookshelf.db;']
        """

        query = "select * from bookshelf.db;"
        return execute(query)
    
    def getById(className:string,id:int):

        """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """

        query = "select * ?  where id=?",className, id
        return execute(query)
    
    def findByTitulo(titulo:string): 
        """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """
            
        query = "select * from bookshelf where title=? ", titulo

        return execute(query)

    def findByAutor(autor:string): 
         """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """
         
        return execute(query)        
    
    def findByGenero(genero:string):
         """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """ 
         
        return execute(query)

    def findByStatus(status:string): 
         """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """
         
        return execute(query)
    
    def findByPeriodoLeitura(periodo:Date): 
         """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """
        
        return execute(query)
    
    def deleteById(id:int): 
         """
        get one iten by its id
        
        :param className: the name of class used (exemple: book, magazine)
        :type className: string
        :param id:
        :type id: int
        """
        
        return execute(query)

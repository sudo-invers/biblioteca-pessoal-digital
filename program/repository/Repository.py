from abc import ABC
from sqlite3 import Date
import string

from program.repository.RepositoryConnection import query

# isso, vai dar sql injection com 100% de certeza;
class Repository(ABC):
    """
    Repositorio base que sera vai extendido nos outros repositorios criados
    """

    def __init__(self):
        self._query = query

    def save(query, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao):
        query = """
                INSERT INTO Obra (titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
        return query
    def getAll():
        return query
    def getById(id:int):
        pass
    def findByTitulo(titulo:string): 
        pass
    def findByAutor(autor:string): 
        pass
    def findByGenero(genero:string): 
        pass
    def findByStatus(status:string): 
        pass
    def findByPeriodoLeitura(periodo:Date): 
        pass
    def deleteById(id:int): 
        pass

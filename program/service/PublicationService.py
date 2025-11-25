from sqlite3 import Date
import sqlite3
from repository.Repository import Repository as repo

import string

class ObraService():
    """
    This class is used to connect what is in the return repository in the controller (which actually the user use).    
    """

    def Save():
        return repo.save()

    def getAll():
        return repo.getAll()
    
    def getById(id:int):

        repo.getById(id)

        if (id is None):
            return sqlite3.Error()
        else:
            return repo.getById()
    
    def findByTitle(title:string):
        return repo.findByTitulo()
    
    def findByAuthor(author:string): 
        return repo.findByAutor()
    
    def findByGenre(genre:string): 
        return repo.findByGenero
    
    def findByStatus(status:int): 
        return repo.findByStatus
    
    def findByPeriodoLeitura(periodo:Date): 
        return repo.findByPeriodoLeitura()
    
    def deleteById(id:int):
        return repo.deleteById()
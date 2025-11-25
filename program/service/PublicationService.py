from sqlite3 import Date
import sqlite3
from repository.Repository import Repository as repo

class PublicationService():
    """
    This class is used to connect what is in the return repository in the controller (which actually the user use).    
    """

    def Save():
        return repo.save()

    def getAll():
        return repo.findAll()
    
    def getById(id:int):

        repo.findById(id)

        if (id is None):
            return sqlite3.Error()
        else:
            return repo.findById()
    
    def findByTitle(title:str):
        return repo.findByTitulo()
    
    def findByAuthor(author:str): 
        return repo.findByAutor()
    
    def findByGenre(genre:str): 
        return repo.findByGenero
    
    def findByStatus(status:int): 
        return repo.findByStatus
    
    def findByPeriodoLeitura(periodo:Date):
        return repo.findByPeriodoLeitura()
    
    def deleteById(id:int):
        return repo.deleteById()
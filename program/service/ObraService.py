from abc import ABC
from sqlite3 import Date
from repository.Repository import Repository as repo

import string

@property
class ObraService(ABC):
    """
    This class is used to connect what is in the repository in the controller (which actually the user use).    
    """

    def Save():
        repo.save()

    def getAll(): 
        repo.getAll()
    
    def getById(id:int):
        repo.getById()
    
    def findByTitle(title:string): 
        repo.findByTitulo()
    
    def findByAuthor(author:string): 
        repo.findByAutor()
    
    def findByGenre(genre:string): 
        repo.findByGenero
    
    def findByStatus(status:int): 
        repo.findByStatus
    
    def findByPeriodoLeitura(periodo:Date): 
        repo.findByPeriodoLeitura()
    
    def deleteById(id:int):
        repo.deleteById()
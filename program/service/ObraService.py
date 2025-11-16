from abc import ABC
from sqlite3 import Date
from repository.Repository import Repository as repo

import string

@property
class ObraService(ABC):
    """
    Classe abstract para ser usada em LivroService e ObraService;
    """

    def criar():
        repo.save()

    def getAll(): 
        repo.getAll()
    
    def getById(id:int):
        repo.getById()
    
    def findByTitulo(titulo:string): 
        repo.findByTitulo()
    
    def findByAutor(autor:string): 
        repo.findByAutor()
    
    def findByGenero(genero:string): 
        repo.findByGenero
    
    def findByStatus(status:int): 
        repo.findByStatus
    
    def findByPeriodoLeitura(periodo:Date): 
        repo.findByPeriodoLeitura()
    
    def deleteById(id:int):
        repo.deleteById()
from datetime import date
from program.repository.Repository import Repository as repo

class PublicationService():
    """
    This class is used to connect what is in the repository to controller    
    """

    def Save():
        return repo.save()

    def getAll():
        return repo.findAll()
    
    def getById(id:int):
        repo.findById(id)

        return repo.findById()
    
    def findByTitle(title:str):
        return repo.findByTitulo()
    
    def findByAuthor(author:str): 
        return repo.findByAutor()
    
    def findByGenre(genre:str): 
        return repo.findByGenero
    
    def findByStatus(status:int): 
        return repo.findByStatus
    
    def findByPeriodoLeitura(periodo:date):
        return repo.findByPeriodoLeitura()
    
    def deleteById(id:int):
        return repo.deleteById()
from abc import ABC
from datetime import date
from program.databases.Repository import Repository as repo

class BaseService(ABC):
    """
    This class is used to connect what is in the repository to controller    
    """

    # This is verrrrrrrrrrrrrrrrrrryyyyyyyyyyyyyyyy big
    def save(
        self,
        title,
        author,
        year,
        type,
        genre,
        inclusionDate,
        pagesNumber,
        status,
        avaliation,
    ):
        return self.repo.save(
            title,
            author,
            year,
            type,
            genre,
            inclusionDate,
            pagesNumber,
            status,
            avaliation,
        )

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
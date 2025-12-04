from abc import ABC

from program.databases.Repository import BaseRepository

class BaseService(ABC):
    """
    This class is used to connect what is in the repository to controller    
    """

    def __init__(self, repository: BaseRepository):
        # O Service recebe o repositório pronto para usar
        self.repo = repository

    def save           (self, title, author, year, type, genre, inclusion_date, pages_number, status, avaliation):
        return self.repo.save(title, author, year, type, genre, inclusion_date, pages_number, status, avaliation)

    def getAll(self):
        return self.repo.findAll()
    
    def getById(self, id: int):
        return self.repo.findById(id)
    
    def findByTitle(self, title: str):
        # Corrigido para chamar o nome em inglês do Repository
        return self.repo.findByTitle(title)
    
    def findByAuthor(self, author: str): 
        return self.repo.findByAuthor(author)
    
    def findByGenre(self, genre: str): 
        return self.repo.findByGenre(genre)
    
    def findByStatus(self, status: str): 
        return self.repo.findByStatus(status)
    
    def deleteById(self, id: int):
        return self.repo.deleteById(id)
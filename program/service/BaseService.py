from abc import ABC

from program.databases.Repository import Repository

class BaseService(ABC):
    """
    This class is used to connect what is in the repository to controller    
    """

    def __init__(self, repository: Repository):
        self.repo = repository
        
    def save(self, title, author, year, genre, pages_number, edition=None, avaliation=None):
        return self.repo.save(
            title=title,
            author=author,
            year=year,
            genre=genre,
            pages_number=pages_number,
            edition=edition,
            avaliation=avaliation,
        )

    def getAll(self):
        return self.repo.getAll()
    
    def getById(self, id: int):
        return self.repo.getById(id)
    
    def getLikeByColumnName(self, column_name: str, status: str): 
        return self.repo.getLikeByColumnName(column_name,status)
    
    def deleteById(self, id: int):
        return self.repo.deleteById(id)

    def publicationPatch(self, id: int, dict: dict):
        return self.repo.putPublication(id, dict)
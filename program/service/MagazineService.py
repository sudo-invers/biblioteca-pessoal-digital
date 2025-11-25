from program.model import Obra
from program.repository import Repository as repo
from ObraService import ObraService

@property
class ObraService(ObraService, Obra):
    
    def __init__(self, id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation, edition):
        super().__init__(id, title, author, year, type, genre, pages_quantity, status, avaliation, anotation)
        
        self._edition= edition

    def getByEdition():
        return repo.getByEdition()


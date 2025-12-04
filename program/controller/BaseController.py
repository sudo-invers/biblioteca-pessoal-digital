from abc import ABC
from program.service.BaseService import BaseService

from fastapi import APIRouter

class BaseController(ABC):

    def __init__(self, service: BaseService, table_name: str):
        self.service = service
        self.table_name = table_name
        self.router = APIRouter(
        prefix=f"/{table_name}", tags=[table_name.capitalize()]
        )
        self._routes()

    def _routes(self): # To not use in others class
        
        @self.router.get("/")
        def getAll():
            return self.service.getAll()
        
        @self.router.get("/{id}")
        def getById(id: int):
            return self.service.getById(id)

        @self.router.get("/author/{author}")
        def getByAuthor(author: str):
            return self.service.getByAuthor(author)

        @self.router.get("/genre/{genre}")
        def getByGenre(genre: str):
            return self.service.getByGenre

        @self.router.get("/status/{status}")
        def getByStatus(status: str):
            return self.service.getByStatus

        @self.router.get("/title/{title}")
        def getByTitle(title: str):
            return self.service.getByTitle
        
        @self.router.delete("/delete/{id}")
        def deletePublicationById(id: int):
            return self.service.deleteById(id)

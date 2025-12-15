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

    def _routes(self): # To not use in others class, that is not controllers

        @self.router.get("/")
        def getAll():
            return self.service.getAll()
        
        @self.router.get("/get/{id}")
        def getById(id: int):
            return self.service.getById(id)

        @self.router.get("/get/search/{column_name}/{value}")
        def getGenericColumn(column_name: str, value ):
            return self.service.getLikeByColumnName(column_name, value)

        @self.router.delete("/delete/{id}")
        def deletePublicationById(id: int):
            return self.service.deleteById(id)

        @self.router.patch("/update/{id}")
        def patchPublication(id: int, dict: dict):
            return self.service.publicationPatch(id, dict)

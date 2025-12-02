from program.schemas.Magazine import Magazine
from program.schemas.Book import Book
from program.service.BaseService import PublicationService as service

from fastapi import FastAPI

from fastapi import APIRouter

router = APIRouter()

app = FastAPI()

class BaseController():

    async def root():
        pass

    @app.get("/publications")
    async def getAll():
        return service.getAll()

    @app.post("/publications/create/book")
    async def createbook(book: Book):
        return service.Save(book)

    @app.post("/publications/create/magazine")
    async def createMagazine(magazine: Magazine):
        return service.Save(magazine)

    @app.delete("/publications/delete")
    async def deletePublicationById(id: int):
        return service.deleteById(id)

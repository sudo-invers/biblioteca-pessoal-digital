from program.domain.Book import Book
from program.domain.Magazine import Magazine
from program.service.PublicationService import PublicationService as service

from fastapi import FastAPI

from fastapi import APIRouter

router = APIRouter()

app = FastAPI()

class PublicationController():

    async def root():
        pass

    @app.get("/publications")
    async def getAll():
        return service.getAll()

    @app.post("/publications/create/book/{book}")
    async def createbook(book: Book):
        return service.Save(book)

    @app.post("/publications/create/magazine/{magazine}")
    async def createMagazine(magazine: Magazine):
        return service.Save(magazine)

    @app.delete("/publications/delete/{id}")
    async def deletePublicationById(id: int):
        return service.deleteById(id)

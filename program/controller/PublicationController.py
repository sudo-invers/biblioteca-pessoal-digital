from fastapi import FastAPI

from program.domain.Book import Book
from program.domain.Magazine import Magazine
from program.service.PublicationService import PublicationService as service

app = FastAPI()

class PublicationController():
    
    @app.get("/")
    def root():
        pass
    @app.get("/publication")
    def getAll():
        return service.getAll()

    @app.post("/publication/book/")
    def createbook():
        return service.Save(Book)

    @app.post("/publication/magazine/")
    def createMagazine():
        service.Save(Magazine)

    @app.delete("/publication/{id}")
    def deleteUserById(id: int):
        pass 

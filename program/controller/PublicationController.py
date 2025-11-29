from program.domain.Book import Book
from program.domain.Magazine import Magazine
from program.service.PublicationService import PublicationService as service

class PublicationController():
    
    async def root():
        pass

    async def getAll():
        return {service.getAll()}

    async def createbook(book: Book) -> Book:
        return {"id": service.Save(book)}

    async def createMagazine(magazine: Magazine) -> Magazine:
        return {"id": service.Save(magazine)}

    async def deleteUserById(id: int) -> int:
        return {"id": service.deleteById(id)}

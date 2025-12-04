from program.controller.BaseController import BaseController
from program.service.BookService import BookService
from program.schemas.Book import Book
from fastapi import HTTPException, status

service = BookService()

controller = BaseController(service, "books")

router = controller.router # Father router

@router.post("/create")
def create_book(book: Book):
    try:
        return service.save(
            title=book.title,
            author=book.author,
            year=book.year,
            type=book.type_.value,
            genre=book.genre,
            inclusionDate=None,
            pagesNumber=book.pages_number,
            status="unread",
            avaliation=book.avaliation,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Could not create the book: {str(e)}"
        )

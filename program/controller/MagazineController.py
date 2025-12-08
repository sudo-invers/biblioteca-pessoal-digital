from fastapi import HTTPException, status
from program.controller.BaseController import BaseController
from program.schemas.Magazine import Magazine
from program.service.MagazineService import MagazineService

service = MagazineService()

controller = BaseController(service, "magazines")

router = controller.router  # Father router

@router.post("/create")
def create_magazine(magazine: Magazine):
    try:
        return service.save(
            title=magazine.title,
            author=magazine.author,
            year=magazine.year,
            genre=magazine.genre,
            pages_number=magazine.pages_number,
            edition=magazine.edition
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Could not create the magazine: {str(e)}"
        )

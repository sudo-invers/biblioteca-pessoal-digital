# program/controller/AnnotationController.py
from fastapi import APIRouter, HTTPException, status
from program.service.AnnotationService import AnnotationService
from program.schemas.AnnotationSchema import Annotation

service = AnnotationService()

router = APIRouter(prefix="/annotations", tags=["Annotations"])

@router.post("/create")
def createAnnotation(annotation: Annotation):
    try:
        return service.save(
            publication_type=annotation.publication_type,
            publication_id=annotation.publication_id,
            page=annotation.page,
            text=annotation.text,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/")
def getAll():
    return service.getAll()


@router.get("/get/{id}")
def getById(id: int):
    return service.getById(id)


@router.get("/publication/{type}/{id}")
def getByPublication(type: str, id: int):
    """
    Args:
        type (str): The publication type (ex: book, magazine)
        id (int): the id of the publication type
    """
    return service.getByPublication(type, id)


@router.get("/publication/{type}/{id}/page/{page}")
def getByPage(type: str, id: int, page: int):
    """
    Args:
        type (str): The publication type (ex: book, magazine)
        id (int): the id of the publication type
        page (int): the page that the annotation is
    """
    return service.getByPage(type, id, page)


@router.delete("/delete/{id}")
def deleteAnnotation(id: int):
    return service.deleteById(id)

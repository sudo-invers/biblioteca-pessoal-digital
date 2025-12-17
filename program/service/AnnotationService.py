from program.databases.AnnotationRepository import AnnotationRepository


class AnnotationService:
    def __init__(self):
        self.repo = AnnotationRepository()

    def save(self, publication_type: str, publication_id: int, page: int, text_content: str):
        return self.repo.save(
            publication_type=publication_type,
            publication_id=publication_id,
            page=page,
            text_content=text_content
        )

    def getAll(self):
        return self.repo.getAll()

    def getById(self, id: int):
        return self.repo.getById(id)

    def getByPublication(self, publication_type: str, publication_id: int):
        return self.repo.getByPublication(publication_type, publication_id)

    def getByPage(self, publication_type: str, publication_id: int, page: int):
        return self.repo.getByPage(publication_type, publication_id, page)

    def deleteById(self, id: int):
        return self.repo.deleteById(id)

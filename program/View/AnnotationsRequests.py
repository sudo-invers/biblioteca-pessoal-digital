from requests import Response
from rich.console import Console
from program.utils.View import Execute

console = Console()

class AnnotationRequests:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        # Execute espera (base_url, table_name)
        self.utils = Execute(self.base_url, "annotations")

    def create(self, publication_type: str, publication_id: int, page: int, text: str) -> Response:
        data = {
            "publication_type": publication_type,
            "publication_id": publication_id,
            "page": page,
            "text": text,
        }
        return self.utils.execute("POST", "create", json_data=data)

    def listByPublication(self, publication_type: str, publication_id: int):
        return self.utils.execute("GET", f"{publication_type}/{publication_id}")

    def listByPage(self, publication_type: str, publication_id: int, page: int):
        return self.utils.execute("GET", f"{publication_type}/{publication_id}/page/{page}")

    def delete(self, annotation_id: int) -> Response:
        return self.utils.execute("DELETE", f"delete/{annotation_id}")

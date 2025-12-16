from datetime import date
from program.databases.DatabaseConnection import RepositoryConnection


class AnnotationRepository:
    def __init__(self):
        self.table = "annotations"

    def save(self, publication_type: str, publication_id: int, page: int, text_content: str):
        # changed :text to :text_content, because text is a reserved keyword in sql, and is more consise
        data = {
            "publication_type": publication_type,
            "publication_id": publication_id,
            "page": page,
            "text_content": text_content,
            "created_at": date.today()
        }

        query = f"""
            INSERT INTO {self.table}
            (publication_type, publication_id, page, text, created_at)
            VALUES (:publication_type, :publication_id, :page, :text_content, :created_at);
        """

        return RepositoryConnection().newQuery(query, data)

    def getAll(self):
        query = f"SELECT * FROM {self.table}"
        return RepositoryConnection().newQuery(query)

    def getById(self, id: int):
        data = {"id": id}
        query = f"SELECT * FROM {self.table} WHERE id = :id;"
        return RepositoryConnection().newQuery(query, data)

    def getByPublication(self, publication_type: str, publication_id: int):
        data = {
            "publication_type": publication_type,
            "publication_id": publication_id
        }

        query = f"""
            SELECT * FROM {self.table}
            WHERE publication_type = :publication_type
            AND publication_id = :publication_id;
        """

        return RepositoryConnection().newQuery(query, data)

    def getByPage(self, publication_type: str, publication_id: int, page: int):
        data = {
            "publication_type": publication_type,
            "publication_id": publication_id,
            "page": page
        }

        query = f"""
            SELECT * FROM {self.table}
            WHERE publication_type = :publication_type
            AND publication_id = :publication_id
            AND page = :page;
        """

        return RepositoryConnection().newQuery(query, data)

    def deleteById(self, id: int):
        data = {"id": id}
        query = f"DELETE FROM {self.table} WHERE id = :id"
        return RepositoryConnection().newQuery(query, data)

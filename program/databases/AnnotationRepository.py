# program/databases/AnnotationRepository.py
from datetime import date
from program.databases.DatabaseConnection import RepositoryConnection

class AnnotationRepository: # Not imported from Repository.py, 
                            # because most os the methods there, will not be utilized
                            # and this will be confuse for me. And is more organized

    def __init__(self):
        self.table = "annotations"

    def save(self, publication_type: str, publication_id: int, page: int, text: str):
        data = {
            "publication_type": publication_type,
            "publication_id": publication_id,
            "page": page,
            "text": text,
            "created_at": date.today(),
        }

        query = f"""
            INSERT INTO {self.table}
            (publication_type, publication_id, page, text, created_at)
            VALUES (:publication_type, :publication_id, :page, :text, :created_at);
        """

        return RepositoryConnection().newQuery(query, data)

    def getAll(self):
        query = f"SELECT * FROM {self.table};"
        
        return RepositoryConnection().newQuery(query)

    def getById(self, id: int):
        data = {"id": id}

        query = f"SELECT * FROM {self.table} WHERE id = :id;"
        
        return RepositoryConnection().newQuery(query, data)

    def getByPublication(self, publication_type: str, publication_id: int):
        data = ({"type": publication_type, "id": publication_id})

        query = f"""
            SELECT * FROM {self.table}
            WHERE publication_type = :type
            AND publication_id = :id;
        """
        
        return RepositoryConnection().newQuery(query, data)

    def getByPage(self, publication_type: str, publication_id: int, page: int):
        data = ({"type": publication_type, "id": publication_id, "page": page})
        
        query = f"""
            SELECT * FROM {self.table}
            WHERE publication_type = :type
            AND publication_id = :id
            AND page = :page;
        
        """
       
        return RepositoryConnection().newQuery(query,data)

    def deleteById(self, id: int):
        data = {"id": id}

        query = f"DELETE FROM {self.table} WHERE id = :id;"
        
        return RepositoryConnection().newQuery(query, data)

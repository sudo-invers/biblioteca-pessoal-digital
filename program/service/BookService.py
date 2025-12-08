from program.databases.Repository import Repository
from program.service.BaseService import BaseService


class BookService(BaseService):
    

    def __init__(self):
        repository = Repository(table_name="books")

        super().__init__(repository)
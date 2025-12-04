from program.databases.Repository import BaseRepository
from program.service.BaseService import BaseService


class BookService(BaseService):
    

    def __init__(self):
        repository = BaseRepository(table_name="books")

        super().__init__(repository)
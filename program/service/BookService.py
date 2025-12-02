from program.databases.Repository import BaseRepository
from program.service.BaseService import BaseService


class BookService(BaseService):

    tableName = BaseRepository(table_name="books")
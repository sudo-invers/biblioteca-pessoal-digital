from typing import override
from program.databases.Repository import BaseRepository
from program.service.BaseService import BaseService


class magazineService(BaseService):
    
    tableName = BaseRepository(table_name="books")

    @override
    def save(
        self,
        title,
        author,
        year,
        type,
        genre,
        inclusionDate,
        pagesNumber,
        status,
        avaliation,
        anotation,
        edition
    ):
        return self.repo.save(
            title,
            author,
            year,
            type,
            genre,
            inclusionDate,
            pagesNumber,
            status,
            avaliation,
            anotation,
            edition
        )

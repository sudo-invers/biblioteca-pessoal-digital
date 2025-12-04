from typing import override
from program.databases.Repository import BaseRepository
from program.service.BaseService import BaseService


class MagazineService(BaseService):

    def __init__(self):
        repository = BaseRepository(table_name="magazines")

        super().__init__(repository)

    @override
    def save(
        self,
        title,
        author,
        year,
        type,
        genre,
        inclusion_date,
        pages_number,
        status,
        avaliation,
        edition
    ):
        return self.repo.save(
            title,
            author,
            year,
            type,
            genre,
            inclusion_date,
            pages_number,
            status,
            avaliation,
            edition
        )

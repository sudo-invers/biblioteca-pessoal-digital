from typing import override
from program.databases.Repository import Repository
from program.service.BaseService import BaseService


class MagazineService(BaseService):

    def __init__(self):
        repository = Repository(table_name="magazines")

        super().__init__(repository)

    @override
    def save(self, title, author, year, genre, pages_number,edition):
        return self.repo.save(title,author,year,genre,pages_number,edition)
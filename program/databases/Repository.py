from program.databases.DatabaseConnection import RepositoryConnection
from utils.utils import sql

class BaseRepository:

    def __init__(self, table_name: str):
        self.bookshelf = sql.table_name(table_name)

    """
    Base repository
    """

    def save(self, title, author, year, type, genre, inclusion_date, pages_number, status, avaliation):

        data = ({
            "title": title,
            "author": author,
            "year": year,
            "type": type,
            "inclusion_date": inclusion_date,
            "genre": genre,
            "pages_number": pages_number,
            "status": status,
            "avaliation": avaliation,
            #"anotation": anotation # Make later
        })

        query = f"""
                INSERT INTO {self.bookshelf} (title, author, year, type, inclusion_date, genre, pages_number, status, avaliation, anotation)
                VALUES (:title, :author, :year, :type, :inclusionDate, :genre, :pagesNumber, :status, :avaliation);
                """
        
        return RepositoryConnection().newQuery(query, data)
    
    def findAll(self):
        """
        debug only
        
        :return: all in the bookshelf
        """

        query = f"select * from {self.bookshelf};"

        return RepositoryConnection().newQuery(query)
    
    def findById(self, id:int):
        data = ({"id": id})

        query = f"select * from {self.bookshelf} where id = :id;"

        return RepositoryConnection().newQuery(query, data)

    def findByTitle(self, title:str): 
        data = ({"title": title})

        query = f"select * from {self.bookshelf} where title like :title;"
        return RepositoryConnection().newQuery(query,data)

    def findByAuthor(self, author:str):
        data = ({"author": author})

        query = f"select * from {self.bookshelf} where author = :author;"
        return RepositoryConnection().newQuery(query, data)

    def findByGenre(self, genre:str):
        data = ({"genre": genre})

        query = f"select * from {self.bookshelf} where genre = :genre;"
        return RepositoryConnection().newQuery(query, data)

    def findByStatus(self, status:str):
        data = ({"status": status})

        query = f"select * from {self.bookshelf} where status where status = :status;"
        
        return RepositoryConnection().newQuery(query, data)

    #def findByReadingPeriod(period:Date): 
        #return 

    def deleteById(self, id:int):
        data = ({"id": id})

        query = f"DELETE FROM {self.bookshelf} WHERE id=:id;"

        if (id is None):
            return None
        else:
            return RepositoryConnection().newQuery(query, data)
        
    def findByWord(self, word:str):
        data = ({"word": word})

        query = f"SELECT * FROM {self.bookshelf} WHERE word=:word;"

        return RepositoryConnection().newQuery(query, data)

    def findBestFivePublications(self):
        query = f"SELECT title, avaliation FROM {self.bookshelf} ORDER BY avaliation DESC LIMIT 5;"

        return RepositoryConnection().newQuery(query)
    
    def findCompletedAverageScore(self):
        query = f"SELECT title, avaliation FROM {self.bookshelf};"

        return RepositoryConnection().newQuery(query)
    
    def findPublicationAmount(self):
        query = f"SELECT COUNT(id) FROM {self.bookshelf};"
        
        return RepositoryConnection().newQuery(query)

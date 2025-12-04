from program.databases.DatabaseConnection import RepositoryConnection

class BaseRepository:

    def __init__(self, table_name: str):
        self.bookshelf = table_name
    """
    Base repository
    """

    def save(self, title, author, year, type, genre, inclusion_date, pages_number, status, avaliation, edition = ""):

        data = ({
            "title": title,
            "author": author,
            "year": year,
            "type": type,
            "inclusion_date": inclusion_date,
            "genre": genre,
            "pages_number": pages_number,
            "status": status,
            "avaliation": avaliation
        })

        if edition != "":  # Goto magazines
            data.update({
                "edition" : edition # Add edition to data dict
            })
            print("Edition detected") # Debug

            query = f"""
            INSERT INTO {self.bookshelf} (title, author, year, type, inclusion_date, genre, pages_number, status, avaliation, edition)
            VALUES (:title, :author, :year, :type, :inclusion_date, :genre, :pages_number, :status, :avaliation, :edition);
            """
    
        else: # Goto books
            query = f"""
                    INSERT INTO {self.bookshelf} (title, author, year, type, inclusion_date, genre, pages_number, status, avaliation)
                    VALUES (:title, :author, :year, :type, :inclusion_date, :genre, :pages_number, :status, :avaliation);
                    """
            
        return RepositoryConnection().newQuery(query, data)
    
    def getAll(self):
        """
        debug only
        
        :return: all in the bookshelf
        """

        query = f"select * from {self.bookshelf};"

        return RepositoryConnection().newQuery(query)
    
    def getById(self, id:int):
        data = ({"id": id})

        query = f"select * from {self.bookshelf} where id = :id;"

        return RepositoryConnection().newQuery(query, data)

    def getByTitle(self, title:str): 
        data = ({"title": title})

        query = f"select * from {self.bookshelf} where title like :title;"
        return RepositoryConnection().newQuery(query,data)

    def getByAuthor(self, author:str):
        data = ({"author": author})

        query = f"select * from {self.bookshelf} where author = :author;"
        return RepositoryConnection().newQuery(query, data)

    def getByGenre(self, genre:str):
        data = ({"genre": genre})

        query = f"select * from {self.bookshelf} where genre = :genre;"
        return RepositoryConnection().newQuery(query, data)

    def getByStatus(self, status:str):
        data = ({"status": status})

        query = f"select * from {self.bookshelf} where status = :status;"
        
        return RepositoryConnection().newQuery(query, data)

    #def getByReadingPeriod(period:Date): 
        #return 

    def deleteById(self, id:int):
        data = ({"id": id})

        query = f"DELETE FROM {self.bookshelf} WHERE id=:id;"

        if (id is None):
            return None
        else:
            return RepositoryConnection().newQuery(query, data)
        
    def getByWord(self, word:str): # Any word that the user like (and no, this will not cause sql injection)
        data = ({"word": word})

        query = f"SELECT * FROM {self.bookshelf} WHERE title LIKE :word;"

        return RepositoryConnection().newQuery(query, data)

    def getBestFivePublications(self):
        query = f"SELECT title, avaliation FROM {self.bookshelf} ORDER BY avaliation DESC LIMIT 5;"

        return RepositoryConnection().newQuery(query)
    
    def getCompletedAverageScore(self):
        query = f"SELECT title, avaliation FROM {self.bookshelf};"

        return RepositoryConnection().newQuery(query)
    
    def getPublicationAmount(self):
        query = f"SELECT COUNT(id) FROM {self.bookshelf};"
        
        return RepositoryConnection().newQuery(query)

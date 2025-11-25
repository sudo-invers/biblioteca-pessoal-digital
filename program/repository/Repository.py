from program.repository.RepositoryConnection import RepositoryConnection

class Repository():

    """
    Repositorio base que sera vai extendido nos outros repositorios criados
    """

    def save(title, author, year, type, genre, inclusionDate, pagesNumber, status, avaliation, anotation):

        data = ({
            "title": title,
            "author": author,
            "year": year,
            "type": type,
            "inclusion_date": inclusionDate,
            "genre": genre,
            "pages_number": pagesNumber,
            "status": status,
            "avaliation": avaliation,
            "anotation": anotation
        })

        query = """
                INSERT INTO bookshelf (title, author, year, type, inclusion_date, genre, pages_number, status, avaliation, anotation)
                VALUES (:title, :author, :year, :type, :inclusionDate, :genre, :pagesNumber, :status, :avaliation, :anotation);
                """
        
        return RepositoryConnection.novaQuery(query, data)
    
    def findAll(tableName:str):
        """
        debug only
        
        :return: all in the bookshelf
        """

        data = ({"table_name": tableName})

        query = "select * from :table_name;"

        return RepositoryConnection.novaQuery(query,data)
    
    def findById(id:int):
        data = ({"id": id})

        query = "select * from bookshelf where id = :id;"

        return RepositoryConnection.novaQuery(query, data)

    def findByTitle(title:str): 
        data = ({"title": title})

        query = "select * from bookshelf where title like :title;"
        return RepositoryConnection.novaQuery(query,data)

    def findByAuthor(author:str):
        data = ({"author": author})

        query = "select * from bookshelf where author where=:author;"
        return RepositoryConnection.novaQuery(query, data)

    def findByGenre(genre:str):
        data = ({"genre": genre})

        query = "select * from bookshelf where genre WHERE genre=:genre;"
        return RepositoryConnection.novaQuery(query, data)

    def findByStatus(status:str):
        data = ({"status": status})
        query = "select * from bookshelf where status where status = :status;"
        
        return RepositoryConnection.novaQuery(query, data)

    #def findByReadingPeriod(period:Date): 
        #return 

    def deleteById(id:int):
        data = ({"id": id})
        query = "DELETE FROM bookshelf WHERE id=:id;"

        if (id is None):
            return None
        else:
            return RepositoryConnection.novaQuery(query, data)
        
    def findByWord(word:str):
        data = ({"word": word})
        query = "SELECT * FROM bookshelf WHERE word=:word"

        return RepositoryConnection.novaQuery(query, data)
    
    def findBestFivePublications():
        query = "SELECT title, avaliation FROM publication ORDER BY avaliation DESC LIMIT 5;"

        return RepositoryConnection.novaQuery(query)
    
    def findCompletedAverageScore():
        query = "SELECT title, avaliation FROM publication"

        return RepositoryConnection.novaQuery(query)
    
    def findPublicationAmount():
        query = "SELECT COUNT(id) FROM publication"
        
        return Repository.novaQuery(query)

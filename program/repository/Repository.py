import string

from program.repository.RepositoryConnection import RepositoryConnection

class Repository():

    """
    Repositorio base que sera vai extendido nos outros repositorios criados
    """
    def save(title, author, year, type, genre, pages_quantity, status, avaliation, anotation):

        """
        Docstring for save
        
        :param name_class: Use os nomes que estão em program.model apenas;
        """

        data = ({
            "title": title,
            "author": author,
            "year": year,
            "type": type,
            "genre": genre,
            "pages_quantity": pages_quantity, 
            "status": status,
            "avaliation": avaliation,
            "anotation": anotation
        })

        query = """
                INSERT INTO bookshelf (title, author, year, type, genre, pages_quantity, status, avaliation, anotation)
                VALUES (:title, :author, :year, :type, :genre, :pages_quantity, :status, :avaliation, :anotation);
                """
        
        return RepositoryConnection.novaQuery(query, data)
    
    def getAll(table_name:string):
        """
        debug only
        
        :return: all in bookshelf
        """

        data = ({
            "table_name": table_name
        })

        query = "select * from :table_name;"

        return RepositoryConnection.novaQuery(query,data)
    
    def getById(id:int) -> int:
        data = ({
            "id": id
        })

        query = "select * from bookshelf where id = :id;"

        return RepositoryConnection.novaQuery(query, data)

    def findByTitle(title:string): 
        data = ({
            "title": title
        })
        query = "select * from bookshelf where title like :title;"
        return RepositoryConnection.novaQuery(query,data)

    def findByAuthor(author:string):
        data = ({
            "author": author
        })
        query = "select * from bookshelf where author like '%:author%';"
        return RepositoryConnection.novaQuery(query, data)

    def findByGenre(genre:string):
        data = ({
            "genre": genre
        })
        query = "select * from bookshelf where genre like '%:genre%';"
        return RepositoryConnection.novaQuery(query, data)

    def findByStatus(status:string):
        data = ({
            "status": status
        })
        query = "select * from bookshelf where status where status = :status;"
        return RepositoryConnection.novaQuery(query, data)

    #def findByReadingPeriod(period:Date): 
    #   return RepositoryConnection.novaQuery(query)

    def deleteById(id:int):
        data = ({
            "id": id
        })
        query = "DELETE FROM bookshelf WHERE id=':id';"

        if (id is None):
            return None
        else:
            return RepositoryConnection.novaQuery(query, data)


from abc import ABC
import sqlite3
from zipapp import create_archive

class RepositoryConnection(ABC):

    def __init__(self, query):
        self._query = query

    def novaQuery(query):
        # Verify if the bookshelf.db exists, if don't, create it;
        try:
            dbLocation = "/databases/bookshelf.db"
            
            if (not dbLocation.exists):
                # Creating the file;
                create_archive(dbLocation)
                # if cannot be created, return a error;
                if (not dbLocation.exists):
                    return FileNotFoundError(f"File '{dbLocation}' not found")
            
            # Conecting to sqlite;
            connection = sqlite3.connect("bookshelf.db")
            cursor = connection.cursor()
            print("DB Init")

            # Execute the query
            cursor.execute(query)

            cursor.close()


        except sqlite3.Error as error:
            # If some error occur, rollback to the last 'good' commit;
            print(f"error - {error} doing rollback")
            cursor.rollback()
        finally:
            # close the  sqlite and commit the channges (if not in rollback);
            if connection:
                connection.commit()
                connection.close()
                print("sucesso")
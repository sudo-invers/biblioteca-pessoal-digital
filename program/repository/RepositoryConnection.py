import sqlite3
import string
from zipapp import create_archive

class RepositoryConnection():

    def novaQuery(query:string, data: string):
        # Verify if the bookshelf.db exists, if don't, create it;
        try:
            dbLocation = "/databases/library.db"
            
            if (not dbLocation.exists):
                # Creating the file;
                create_archive(dbLocation)
                # if cannot be created, return a error;
                if (not dbLocation.exists):
                    return FileNotFoundError(f"File '{dbLocation}' not found")
            
            if (data is not None):
                # Conecting to sqlite;
                connection = sqlite3.connect("library.db")
                cursor = connection.cursor()
                print("DB INIT SUCCESS")

                # Execute the query and the data params
                cursor.executemany(query,data)

                cursor.close()
            else:
            
                # Conecting to sqlite;
                connection = sqlite3.connect("library.db")
                cursor = connection.cursor()
                print("DB INIT SUCCESS")

                # Execute the execute
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
                print("SUCESS")
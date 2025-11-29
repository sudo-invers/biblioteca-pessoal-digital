import sqlite3
import string

class RepositoryConnection():

    def novaQuery(query:string, data: string):

        try:
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
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class RepositoryConnection:
    """
        Connects to the library repository, and make querys
    """
    # Switched from pure sqlite3, to sqlAlchemy for security reasons
    # Maybe later i will try using the ORM in its full potencial, but for now, it will not make a diference

    def __init__(self, database_url: str = "sqlite:///library.db"):
        self.engine = create_engine(database_url, echo=True)
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

    def newQuery(self, query: str,  data: dict | list[dict] | None = None):
        session = self.SessionLocal()
        try:
            print("DB INITIALIZED WITH SUCCESS")

            if data is not None:
                # Execute the query and the data params
                session.execute(text(query), data)
            else:
                # Execute the query
                session.execute(text(query))

            session.commit()
            print("CHANGES MADE WITH SUCESS")

        except Exception as error:
            print(f"error - {error} doing rollback")
            session.rollback()

        finally:
            session.close()
            print("CONNECTION CLOSED")


# Delete in the next release
"""class RepositoryConnection():

    def newQuery(self, query:str, data: str):

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
                print("DB INITIALIZED WITH SUCCESS")

                # Execute the execute one
                cursor.execute(query)

                cursor.close()

        except sqlite3.Error as error:
            # If some error occur, rollback to the last 'good' commit;
            print(f"error - {error} doing rollback")
            connection.rollback()
        finally:
            # close the  sqlite and commit the channges (if not in rollback);
            if connection:
                connection.commit()
                connection.close()
                print("CHANGES MADE")
"""     




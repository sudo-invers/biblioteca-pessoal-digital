from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from program.domain.Base import Base

# I am not using, but it create the tables if not exist
from program.domain.Book import Book  # noqa: F401
from program.domain.Magazine import Magazine  # noqa: F401


class RepositoryConnection:
    """
        Connects to the library repository, and make querys
    """
    # Switched from pure sqlite3, to sqlAlchemy for security reasons
    # Maybe later i will try using the ORM in its full potencial, but for now, it will not make a diference

    _engine = create_engine("sqlite:///library.db", echo=True)
    _SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)

    def __init__(self):
        print("Verifing database...")
        Base.metadata.create_all(self._engine) # If it exist, don't recreate again
        print("Database is ready!")

    def newQuery(self, query: str,  data: dict | list[dict] | None = None):
        session = self.SessionLocal()
        try:
            print("DB INITIALIZED WITH SUCCESS")

            #Execute 'Select' query
            if query.strip().upper().startswith("SELECT"):
                result = session.fetchall()
                return result

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
            return None

        finally:
            session.close()
            print("CONNECTION CLOSED")

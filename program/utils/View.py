from rich.console import Console
from sqlalchemy import create_engine, inspect

DB_URL = "sqlite:///library.db"

class ViewUtils:

    def selectPublicationTypeAndId(self, table_name: str, id_pub: int):
        table_name.lower()
        if table_name == "book":
            return self.req_book.getById(id_pub)
        elif table_name == "magazine":
            return self.req_magazine.getById(id_pub)
        else:
            Console.print(f"[red]Table '{table_name}' doesn't exist[/red]")
            return None
    
    def selectAllPublicationByType(self, table_name):
        if table_name == "book" or table_name == "books" :
            return self.req_book.getAll()
        elif table_name == "magazine" or table_name == "magazines":
            return self.req_magazine.getAll()
        else:
            Console.print(f"[red]Table '{table_name}' don't exist[/red]")
            return
    def getTableNames(table_name: str) -> list[str]:
        """
        Returns all columns names of a table 
        """
        engine = create_engine(DB_URL)
        inspector = inspect(engine)

        try:
            columns = inspector.get_columns(table_name)
            return [col["name"] for col in columns]
        except Exception as e:
            print(f"Error in obtaining: '{table_name}': {e}")
            return []
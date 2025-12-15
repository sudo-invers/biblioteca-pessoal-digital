from rich.console import Console
from urllib.parse import quote
from program.utils.View import Execute

console = Console()

class HttpRequest:
    def __init__(self, table_name: str, base_url: str):
        self.table_name = table_name
        self.base_url = base_url.rstrip("/")
        self.timeout = 5
        self.utils = Execute(base_url, table_name)

    def getAll(self):
        return self.utils.execute("GET", "")

    def getByWord(self,colums_name: str, text: str):
        """
        Args:
            colums_name (str): the name of the columm to search (in the db). EX: author
            text (str): the text to search

        Returns:
            _type_: _description_
        """
        safe_text = quote(text)  # Transforms special caracters in a safe format, example space = %20 
        return self.utils.execute("GET", f"get/search/{colums_name}/{safe_text}") # Example:  "get/search/title/dovakin dragonborn" to "get/tile/dovakin%20dragonborn" to not break the url"

    def getById(self, id: int):
        return self.utils.execute("GET", f"get/{id}")

    def post(self, data: dict):
        """Send a JSON dict to /create"""
        return self.utils.execute("POST", "create", json_data=data)

    def delete(self, id: int):
        return self.utils.execute("DELETE", f"delete/{id}")
    
    def updatePut(self, id: int, data: dict):
        """
        Probrably, i am not using it
        """
        return self.utils.execute("PUT", f"update/{id}", json_data=data)

    def updatePatch(self, id: int, data: dict):
        """
        Update a record with the given id.
        Sends JSON data to /update/{id} using HTTP patch
        """
        return self.utils.execute("PATCH", f"update/{id}", json_data=data)

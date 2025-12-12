import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

from rich.console import Console
from urllib.parse import quote

console = Console()


class HttpRequest:
    def __init__(self, table_name: str, base_url: str):
        self.table_name = table_name
        self.base_url = base_url.rstrip("/")
        self.timeout = 5

    def _execute(self, method: str, endpoint: str, json_data: dict = None):
        """
        Args:
            method (str): HTTP action (ex: "GET", "POST", "DELETE").
            endpoint (str): Query url end
            json_data (dict): The data for post method
        example:
            method = "GET", endpoint = "The Book of arts"
            query = get/The Book of arts

        Returns:
            _type_: HTTP request
        """
        url = f"{self.base_url}/{self.table_name}/{endpoint}".rstrip("/")

        try:
            response = requests.request(method, url, timeout=self.timeout, json=json_data)
            return response

        except ConnectionError:
            console.print(
                f"[bold red]Connection error:[/bold red] cannot connect to: {self.base_url}"
            )
            return self._mock_error_response(503, "Service not disponible")
        except Timeout:
            console.print(
                "[bold red]Timeout:[/bold red] The server took a long time to respond."
            )
            return self._mock_error_response(504, "Timeout")
        except RequestException as e:
            console.print(f"[bold red]Request error: [/bold red] {e}")
            return self._mock_error_response(500, str(e))

    def _mock_error_response(self, status_code, message):
        """Create a 'false' response, to not break the code."""

        class MockResponse: # ...This is complicated
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

            @property
            def text(self):
                return str(self.json_data)

        return MockResponse({"detail": message}, status_code)

    def getAll(self):
        return self._execute("GET", "")

    def getByWord(self,colums_name: str, text: str):
        """
        Args:
            colums_name (str): the name of the columm to search (in the db). EX: author
            text (str): the text to search

        Returns:
            _type_: _description_
        """
        safe_text = quote(text)  # Transforms special caracters in a safe format, example space = %20 
        return self._execute("GET", f"get/{colums_name}/{safe_text}") # Example:  "get/title/dovakin dragonborn" to "get/tile/dovakin%20dragonborn" to not break the url"

    def getById(self, id: int):
        return self._execute("GET", f"get/{id}")

    def post(self, data: dict):
        """Send a JSON dict to /create"""
        return self._execute("POST", "create", json_data=data)

    def delete(self, id: int):
        return self._execute("DELETE", f"delete/{id}")
    
    def updatePut(self, id: int, data: dict):
        """
        Probrably, i am not using it
        """
        return self._execute("PUT", f"update/{id}", json_data=data)

    def updatePatch(self, id: int, data: dict):
        """
        Update a record with the given id.
        Sends JSON data to /update/{id} using HTTP patch
        """
        return self._execute("PATCH", f"update/{id}", json_data=data)

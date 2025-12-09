import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

from rich.console import Console
from urllib.parse import quote

console = Console()


class HttpRequest:
    def __init__(self, table_name: str, base_url: str):
        self.table_name = table_name
        self.base_url = base_url.rstrip("/")
        # Timeout evita que o programa congele se o servidor demorar
        self.timeout = 5

    def _execute(self, method: str, endpoint: str, json_data: dict = None):
        """_summary_

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
        """Create a 'false' response, for not break the code."""

        class MockResponse:
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

    def getByVariable(self, text: str): 
        safe_text = quote(text)  # Transforms special caracters in a safe format, example space = %20 
        return self._execute("GET", f"get/{safe_text}") # Example:  "dovakin dragonborn" to "dovakin%20dragonborn" to not break the url"

    def getById(self, id: int):
        return self._execute("GET", f"get/{id}")

    def post(self, data: dict):
        """Send a JSON dict to /create"""
        return self._execute("POST", "create", json_data=data)

    def delete(self, id: int):
        return self._execute("DELETE", f"delete/{id}")


"""

Testing new HttpRequest class, maybe i switch later

class HttpRequest():

    def __init__(self, table_name: str, base_url: str):
        self.table_name = table_name
        self.base_url = base_url.rstrip("/")  # "http://0.0.0.0:8000

    def getAll(self):
        request = requests.get(f"{self.base_url}/{self.table_name}/")

        return request

    def getByVariable(self, string: str):
        request = requests.get(f"{self.base_url}/{self.table_name}/get/{string}")

        return request

    def getById(self, id:int):
            request = requests.get(f"{self.base_url}/{self.table_name}/get/{id}")

            return request

    def post(self, string: str):
        request = requests.post(f"{self.base_url}/{self.table_name}/post/{string}")

        return request

    def delete(self, id: int):
        request = requests.delete(f"{self.base_url}/{self.table_name}/delete/{id}")

        return request

"""
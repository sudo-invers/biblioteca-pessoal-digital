import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
from sqlalchemy import create_engine, inspect
from rich.prompt import Prompt
from rich.console import Console

console = Console()

DB_URL = "sqlite:///library.db"

class ViewUtils:

    def visualizeColumnsNames(table_name: str):
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
    
    def promptAskQuantity(self, choicesQuantity: int):
        choices = []
        for i in range(0, choicesQuantity, 1):
            choices.append(f"{i}") 
        prompt = Prompt.ask("\n Write the option number", choices=choices)
        return prompt

    def validateNotEmpty(text: str) -> bool:
        """Valida se o texto NÃO é vazio (usado para campos obrigatórios)."""
        return bool(text.strip())


class Execute:
    def __init__(self, base_url: str, table_name: str, timeout: int = 5):
        self.base_url = base_url.rstrip("/")
        self.table_name = table_name
        self.timeout = timeout

    def execute(self, method: str, endpoint: str, json_data: dict = None):
        url = f"{self.base_url}/{self.table_name}/{endpoint}".rstrip("/")

        try:
            return requests.request(method, url, timeout=self.timeout, json=json_data)

        except ConnectionError:
            console.print(
                f"[bold red]Connection error:[/bold red] cannot connect to: {self.base_url}"
            )
            return self._mock_error_response(503, "Service not available")

        except Timeout:
            console.print(
                "[bold red]Timeout:[/bold red] The server took a long time to respond."
            )
            return self._mock_error_response(504, "Timeout")

        except RequestException as e:
            console.print(f"[bold red]Request error:[/bold red] {e}")
            return self._mock_error_response(500, str(e))

    def _mock_error_response(self, status_code, message):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self._json = json_data
                self.status_code = status_code

            def json(self):
                return self._json

            @property
            def text(self):
                return str(self._json)

        return MockResponse({"detail": message}, status_code)
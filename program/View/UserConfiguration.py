import json
from rich.console import Console
from rich.prompt import Prompt, IntPrompt

console = Console()


# This class is so small, that i decided to not make a request and comands separeted classes
class RequestsUserConfiguration:
    DEFAULT_CONFIG = {
        "favorite genre": "",
        "limit of simultaneous pages": 0,
        "annual reading goal": 0,
    }

    def __init__(self, config_file: str = "program.user_config.json"):
        self.config_file = config_file
        self.user_config = self._load()

    def _load(self) -> dict:
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            console.print(
                f"[yellow]{self.config_file} not found. Using default configuration.[/yellow]"
            )
            return self.DEFAULT_CONFIG.copy()
        except json.JSONDecodeError:
            console.print(
                f"[red]Invalid JSON in {self.config_file}. Using default configuration.[/red]"
            )
            return self.DEFAULT_CONFIG.copy()

    def _save(self) -> None:
        try:
            with open(self.config_file, "w") as file:
                json.dump(self.user_config, file, indent=4)
            console.print("[bold green]Configuration saved successfully![/bold green]")
        except Exception as e:
            console.print(f"[red]Error saving configuration: {e}[/red]")

    def show(self) -> None:
        console.print("[bold blue]--- Current User Configuration ---[/bold blue]")
        for key, value in self.user_config.items():
            console.print(f"{key.capitalize()}: {value}")

    def update(self) -> None:
        self.show()

        field = Prompt.ask(
            "Which field would you like to update?",
            choices=list(self.user_config.keys()),
        )

        if field == "favorite genre":
            self._update_favorite_genre()

        elif field == "limit of simultaneous pages":
            self._update_limit_pages()

        elif field == "annual reading goal":
            self._update_annual_goal()

        self._save()

    def _update_favorite_genre(self) -> None:
        new_value = Prompt.ask(
            "Enter the new favorite genre (leave empty to keep current)"
        ).strip()

        if new_value:
            self.user_config["favorite genre"] = new_value.lower()

    def _update_limit_pages(self) -> None:
        new_value = IntPrompt.ask("Enter the new limit of simultaneous pages")
        self.user_config["limit of simultaneous pages"] = new_value

    def _update_annual_goal(self) -> None:
        new_value = IntPrompt.ask("Enter the new annual reading goal")
        self.user_config["annual reading goal"] = new_value

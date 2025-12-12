import json
from rich.console import Console
from rich.prompt import Prompt, IntPrompt

console = Console()

class RequestsUserConfiguration:
    def __init__(self, config_file="program.user_config.json"):
        self.config_file = config_file

    def load(self):
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            console.print(
                f"[red]Error: {self.config_file} not found. Using default configuration.[/red]"
            )
            return {
                "favorite genre": "",
                "limit of simultaneous pages": 0,
                "annual reading goal": 0,
            }
        except json.JSONDecodeError:
            console.print(f"[red]Error: Could not parse {self.config_file}.[/red]")
            return {
                "favorite genre": "",
                "limit of simultaneous pages": 0,
                "annual reading goal": 0
            }

    def save(self):
        try:
            with open(self.config_file, "w") as file:
                json.dump(self.user_config, file, indent=4)
            console.print(
                "[bold green]Configuration updated and saved successfully![/bold green]"
            )
        except Exception as e:
            console.print(f"[red]Error saving the configuration: {e}[/red]")

    def update(self):
        console.print("[bold blue]--- Current User Configuration ---[/bold blue]")
        for key, value in self.user_config.items():
            console.print(f"{key.capitalize()}: {value}")

        field_to_update = Prompt.ask(
            "[yellow]Which field would you like to update? (favorite genre, limit of simultaneous pages, annual reading goal)[/yellow]"
        ).lower()

        if field_to_update not in self.user_config:
            console.print(
                "[red]Invalid field name. Please choose from 'favorite genre', 'limit of simultaneous pages', or 'annual reading goal'.[/red]"
            )
            return

        if field_to_update == "favorite genre":
            new_value = Prompt.ask("Enter the new favorite genre (leave empty to not change): ").lower().strip()
            if (new_value.startswith("")):
                pass
            else:
                self.user_config[field_to_update] = new_value

        elif field_to_update == "limit of simultaneous pages":
            new_value = IntPrompt.ask("Enter the new limit of simultaneous pages: ").lower().strip()
            if (new_value.strip().startswith("")):
                new_value = ""
            else:
                self.user_config[field_to_update] = new_value

        elif field_to_update == "annual reading goal":
            new_value = IntPrompt.ask("Enter the new annual reading goal: ").lower().strip()
            if (new_value.strip().startswith("")):
                pass
            else:
                self.user_config[field_to_update] = new_value
        self.save_user_config()

        console.print("\n[bold green]Configuration updated successfully![/bold green]")
        for key, value in self.user_config.items():
            console.print(f"{key.capitalize()}: {value}")

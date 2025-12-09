import sys

from rich import print as rprint
from rich.console import Console
from rich.prompt import Prompt

from program.View.Comands import Comands

console = Console()


class CLI:
    def __init__(self):
        self.comands = Comands()

    def run(self):
        while True:
            console.clear()

            console.print(
                "[bold cyan]--- publication manager ---[/bold cyan]",
                justify="center"
            )

            # Options
            console.print("\n[bold]Choose what you wanna do today (:[/bold]")
            console.print("[1] Create Book")
            console.print("[2] Create Magazine")
            console.print("[3] Create Collection { For now, it don't work.... ): }")
            console.print("[sea_green2]-------------------------[/sea_green2]")
            console.print("[4] List all publications")
            console.print("[5] List publication (id)")
            console.print("[light_sky_blue1]-------------------------[/light_sky_blue1]")
            console.print("[6] Delete Book")
            console.print("[7] Delete Magazine")
            #console.print("[8] search publication by word")
            console.print("[red]-------------------------[/red]")
            console.print("[0] Exit")

            # User input
            action = Prompt.ask(
                "\n Write the option number", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8"]
            )

            self.handle_action(action)

    def handle_action(self, action: str):
        if action == "0":
            console.print("[red]Exiting...[/red]")
            sys.exit()
        elif action == "1":
            self.comands.createBook()
        elif action == "2":
            self.comands.createMagazine()
        elif action == "3":
            self.comands.createCollection()
        elif action == "4":
            self.comands.getAllPublications()
        elif action == "5":
            self.comands.getPublicationById()
        elif action == "6":
            self.comands.deleteBookById()
        elif action == "7":
            self.comands.deleteMagazineById()
        # elif action == "8":
        #     self.comands.filterByWord()

if __name__ == "__main__":
    # Conection test
    rprint("[bold white on blue] STATIRG CLIENT [/bold white on blue]")
    try:
        app = CLI()
        app.run()
    except KeyboardInterrupt: # Example, ctrl + c
        rprint("\n[bold red]Interrupted.[/bold red]")

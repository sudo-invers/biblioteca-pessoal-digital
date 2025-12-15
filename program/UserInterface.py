import sys

from rich import print as rprint
from rich.console import Console

from program.View.Comands import Comands
from program.View.AnnotationsComands import AnnotationCommands
from program.View.RequestsUserConfiguration import RequestsUserConfiguration
from program.utils.View import ViewUtils

console = Console()

class CLI:
    def __init__(self):
        self.utils = ViewUtils()
        self.comands = Comands()
        self.annotations = AnnotationCommands()
        self.config = RequestsUserConfiguration()

    def run(self):
        while True:
            console.clear()

            console.print(
                "[bold cyan]--- publication manager ---[/bold cyan]", justify="center"
            )

            # Options
            console.print("\n[bold]Choose what you wanna do today (:[/bold]")
            console.print("[1] Create Publication")
            console.print("[sea_green2]-------------------------[/sea_green2]")
            console.print("[2] List publications")
            console.print("[light_sky_blue1]-------------------------[/light_sky_blue1]")
            console.print("[3] Delete Publication")
            console.print("[green]-------------------------[/green]")
            console.print("[4] Update Publication")
            console.print("[green]-------------------------[/green]")
            console.print("[5] configurations]")
            console.print("[purple]-------------------------[/purple]")
            console.print("[6] Annotations")
            console.print("[red]-------------------------[/red]")
            console.print("[0] Exit")

            # User input
            action1 = self.utils.promptAskQuantity(7)
            action3 = "None"

            if action1 == "0":
                action2 = "0"

            if action1 == "1":
                console.print("[0] Back")
                console.print("[1] Create Book")
                console.print("[2] Create Magazine")
                console.print("[3] Create Collection")
                action2 = self.utils.promptAskQuantity(4)

            if action1 == "2":
                console.print("[0] Back")
                console.print("[1] list Books")
                console.print("[2] list Magazines")
                action2 = self.utils.promptAskQuantity(3)

            if action1 == "3":
                console.print("[0] Back")
                console.print("[1] delete Book")
                console.print("[2] delete Magazine")
                action2 = self.utils.promptAskQuantity(3)

            if action1 == "4":
                console.print("[0] Back")
                console.print("[1] Update Book")
                console.print("[2] Update Magazine")
                action2 = self.utils.promptAskQuantity(3)

            if action1 == "5":
                console.print("[0] Back")
                console.print("[1] Update Magazine")
                action2 = self.utils.promptAskQuantity(2)
            
            if action1 == "6":
                console.print("[0] Back")
                console.print("[1] Create annotation")
                console.print("[2] List annotations")
                console.print("[3] Delete annotation")
                action2 = self.utils.promptAskQuantity(4)
                
                if action2 == "1":
                    console.print("[0] Back")
                    console.print("[1] Create book annotation")
                    console.print("[2] Create magazine annotation")
                    action3 = self.utils.promptAskQuantity(3)
                if action2 == "2":
                    console.print("[0] Back")
                    console.print("[1] List  book annotations")
                    console.print("[2] List magazine annotations")
                    action3 = self.utils.promptAskQuantity(3)
                if action2 == "3":
                    console.print("[0] Back")
                    console.print("[1] Delete book annotation")
                    console.print("[2] Delete magazine annotation")
                    action3 = self.utils.promptAskQuantity(3)
            self.handle_action1(action1, action2, action3)

    def handle_action1(self, action1: str, action2: str, action3: str):
        if action1 == "0":
            console.print("[red]Exiting...[/red]")
            sys.exit()
        elif action1 == "1":
            if action2 == "1":
                self.comands.createBook()
            elif action2 == "2":
                self.comands.createMagazine()
            elif action2 == "3":
                self.comands.createCollection()

        elif action1 == "2":
            if action2 == "1":
                self.comands.getAllPublications("book")
            elif action2 == "2":
                self.comands.getAllPublications("magazine")

        elif action1 == "3":
            if action2 == "1":
                self.comands.deleteBookById()
            elif action2 == "2":
                self.comands.deleteMagazineById()

        elif action1 == "4":
            if action2 == "1":
                self.comands.updatePatch("book")
            elif action2 == "2":
                self.comands.updatePatch("magazine")

        elif action1 == "5":
            if action2 == "1":
                self.config.load()
            elif action2 == "2":
                self.config.update()

        elif action1 == "6":
            if action2 == "1":
                if action3 == "1":
                    self.annotations.create("book")
                elif action3 == "2":
                    self.annotations.create("magazine")
            
            if action2 == "2":
                if action3 == "1":
                    self.annotations.list("book")
                elif action3 == "2":
                    self.annotations.list("magazine")
            
            if action2 == "3":
                if action3 == "1":
                    self.annotations.delete("books")                    
                elif action3 == "2":
                    self.annotations.delete("magazines")


if __name__ == "__main__":
    # Conection test
    rprint("[bold white on blue] STATIRG CLIENT [/bold white on blue]")
    try:
        app = CLI()
        app.run()
    except KeyboardInterrupt:  # Example, ctrl + c
        rprint("\n[bold red]Interrupted.[/bold red]")

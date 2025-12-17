from rich import print as rprint
from program.UserInterface import CLI

if __name__ == "__main__":
    # Conection test
    rprint("[bold white on blue] STATIRG CLIENT [/bold white on blue]")
    try:
        CLI().run()
        
    except KeyboardInterrupt:  # Example, ctrl + c
        rprint("\n[bold red]Interrupted.[/bold red]")

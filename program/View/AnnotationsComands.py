# program/View/AnnotationCommands.py
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from program.View.AnnotationsRequests import AnnotationRequests

console = Console()
BASE_URL = "http://127.0.0.1:8000"

class AnnotationCommands:
    def __init__(self):
        self.annotations = AnnotationRequests(BASE_URL)

    def create(self, pub_type: str):
        console.print("[bold blue]--- Create annotation ---[/bold blue]")

        pub_id = IntPrompt.ask("Publication ID")
        page = IntPrompt.ask("Page")
        text = Prompt.ask("Annotation text")

        response = self.annotations.create(pub_type, pub_id, page, text)

        if getattr(response, "status_code", None) in (200, 201):
            console.print("[bold green]Annotation created successfully[/bold green]")
        else:
            console.print(f"[red]Failed:[/red] {getattr(response, 'text', response)}")

    def list(self, pub_type: str):
        console.print("[bold blue]--- List annotations ---[/bold blue]")

        pub_id = IntPrompt.ask("Publication ID")

        filter_page = Prompt.ask(
            "Filter by page? (y/n)", choices=["y", "n"], default="n"
        )
        if filter_page == "y":
            page = IntPrompt.ask("Page")
            response = self.annotations.listByPage(pub_type, pub_id, page)
        else:
            response = self.annotations.listByPublication(pub_type, pub_id)

        if getattr(response, "status_code", None) != 200:
            console.print(f"[red]Error:[/red] {getattr(response, 'text', response)}")
            return

        data = response.json()
        if not data:
            console.print("[yellow]No annotations found.[/yellow]")
            return

        if isinstance(data, dict):
            data = [data]

        table = Table(title=f"Annotations for {pub_type.capitalize()} {pub_id}", show_lines=True)
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("Page", justify="center")
        table.add_column("Text", overflow="fold", width=50)
        table.add_column("Created At", justify="center")

        for annotation in data:
            table.add_row(
                str(annotation.get("id", "-")),
                str(annotation.get("page", "-")),
                str(annotation.get("text", "")),
                str(annotation.get("created_at", "-")),
            )
        if len(data) > 0:
            with console.pager(styles=True):
                console.print(table)
        else:
            console.print("[yellow]No annotations found.[/yellow]")

    def delete(self):
        console.print("[bold red]--- Delete annotation ---[/bold red]")
        annotation_id = IntPrompt.ask("Annotation ID")
        response = self.annotations.delete(annotation_id)

        if getattr(response, "status_code", None) == 200:
            console.print("[bold green]Annotation deleted successfully[/bold green]")
        else:
            console.print(f"[red]Failed:[/red] {getattr(response, 'text', response)}")

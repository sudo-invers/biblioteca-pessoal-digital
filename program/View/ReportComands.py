from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt

from program.service.ReportService import ReportService
from program.View.ReportStorage import ReportStorage

console = Console()


class ReportCommands:
    def __init__(self):
        self.service = ReportService()
        self.storage = ReportStorage()

    def generate(self):
        report = self.service.generateReport()
        filename = self.storage.save(report)
        console.print(f"[green]Report generated: {filename}[/green]")

    def list(self):
        reports = self.storage.listReports()

        if not reports:
            console.print("[yellow]No reports available.[/yellow]")
            return

        table = Table(title="Available Reports")
        table.add_column("#", justify="right")
        table.add_column("File name")

        for i, name in enumerate(reports, start=1):
            table.add_row(str(i), name)

        console.print(table)

    def show(self):
        reports = self.storage.listReports()

        if not reports:
            console.print("[yellow]No reports available.[/yellow]")
            return

        self.list()

        try:
            choice = IntPrompt.ask(
                "Select a report number",
                choices=[str(i) for i in range(1, len(reports) + 1)],
            )
        except Exception:
            return

        data = self.storage.load(reports[choice - 1])
        if not data:
            console.print("[red]Error loading data[/red]")
            return

        report = data["report"]

        console.print(f"\n[bold cyan]Generated at:[/bold cyan] {data['generatedAt']}")
        console.print(f"[bold]Total publications:[/bold] {report['totalPublications']}")

        table = Table(title="Publication Status")
        table.add_column("Status")
        table.add_column("Quantity", justify="right")
        table.add_column("Percentage", justify="right")

        for status, values in report["statusSummary"].items():
            table.add_row(status, str(values["quantity"]), f"{values['percentage']}%")

        console.print(table)

        console.print(
            f"\n[bold]Average rating (completed):[/bold] {report['averageRatingCompleted']}"
        )

        top = Table(title="Top 5 Best Rated")
        top.add_column("Title")
        top.add_column("Type")
        top.add_column("Rating", justify="right")

        for item in report["top5BestRated"]:
            top.add_row(item["title"], item["type"], str(item["avaliation"]))

        console.print(top)

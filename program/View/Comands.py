from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from program.View.Requests import HttpRequest
from program.utils.View import ViewUtils as utils

console = Console()

BASE_URL = "http://127.0.0.1:8000"

class Comands:
    def __init__(self):
        self.req_book = HttpRequest("books", BASE_URL)
        self.req_magazine = HttpRequest("magazines", BASE_URL)
    def createBook(self):
        console.print("[bold blue]--- New book ---[/bold blue]")
        console.print("--- You can ignore year and pages if you want ---")
        
        title = Prompt.ask("Title: ")
        author = Prompt.ask("Author: ")
        year = IntPrompt.ask("Publication year: ") 
        pages = IntPrompt.ask("number of pages: ")
        genre = Prompt.ask("Genre: ")

        book_data = {
            "title": title,
            "author": author,
            "year": year,
            "pages_number": pages,
            "genre": genre,
            "avaliation": 5 # can update later
        }

        response = self.req_book.post(book_data)
        self._show_response(response)

    def createMagazine(self):
        console.print("[bold blue]--- New magazine ---[/bold blue]")
        console.print("--- You can ignore year and pages if you want ---")

        title = Prompt.ask("Title: ")
        author = Prompt.ask("Author: ")
        year = IntPrompt.ask("Publication year: ")
        pages = IntPrompt.ask("number of pages: ")
        edition = IntPrompt.ask("edition: ")

        book_data = {
            "title": title,
            "author": author,
            "year": year,
            "pages_number": pages,
            "edition": edition,
            "avaliation": 5  # can update later
        }

        response = self.req_book.post(book_data)
        self._show_response(response)

    def createCollection(self):
        console.print(
            "[yellow]Current in development...[/yellow]"
        )
        pass

    def getAllPublications(self):
        console.print("[bold blue]--- Loading publications... ---[/bold blue]")

        table_name = Prompt.ask("View all (Book or Magazine): ").lower()

        response = self.ViewUtils.selectAllPublicationByType(table_name) # Testing using self in a variable

        if response.status_code == 200:
            data = response.json()
            
            # Create a table uwu
            table = Table(title=f"All {table_name}s")

            # Add colums;       # This shit is verrrrrry prettttyyy awaaaaaaaaaaaaaa
            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("Title", style="magenta")
            table.add_column("Author", style="green")
            table.add_column("Year", justify="center")
            table.add_column("Pages", justify="center")
            table.add_column("Genre", justify="center")
            table.add_column("Avaliation", justify="center")

            # Make the lines
            for item in data:
                table.add_row( # The table can only accept strings
                    str(item.get("id", "-")), 
                    (item.get("title", "Not Found")),
                    (item.get("author", "Unknow")),
                    str(item.get("year", "-")),
                    str(item.get("pages_number", "0")),
                    str(item.get("genre", "Unknow")),
                    str(item.get("avaliation", "0"))
                )

            with console.pager(styles=True):
                console.print(table)
                
        else:
            console.print(f"[red]Error:[/red] {response.status_code}")

    def getPublicationById(self):
        console.print("[bold blue]--- Loading publication... ---[/bold blue]")

        table_name = Prompt.ask("Book or Magazine").lower()
        id_pub = Prompt.ask("id")

        response = None 

        if table_name == "book":
            response = self.req_book.getById(id_pub)
        elif table_name == "magazine":
            response = self.req_magazine.getById(id_pub)
        else:
            console.print(f"[red]Table '{table_name}' doesn't exist[/red]")
            return

        if response and response.status_code == 200:
            data = response.json()

            if isinstance(data, dict):
                data = [data]

            table = Table(title=f"{table_name.capitalize()} details")

            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("Title", style="magenta")
            table.add_column("Author", style="green")
            table.add_column("Year", justify="center")
            table.add_column("Pages", justify="center")
            table.add_column("Genre", justify="center")
            table.add_column("Rating", justify="center")
            
            if table_name == "magazine":
                table.add_column("Edition", justify="center", style="yellow")

            for item in data:

                row_data = [
                    str(item.get("id", "-")),
                    item.get("title", "Not Found"),
                    item.get("author", "Unknown"),
                    str(item.get("year", "-")),
                    str(item.get("pages_number", "0")),
                    str(item.get("genre", "Unknown")),
                    str(item.get("avaliation", "0"))
                ]

                if table_name == "magazine":
                    row_data.append(str(item.get("edition", "-")))

                table.add_row(*row_data)

            console.print(table)

        else:
            code = response.status_code if response else "Error"
            console.print(f"[red]Error:[/red] {code}")

    def _show_response(self, response):
        if response.status_code in [200, 201]:
            console.print("[bold green]Success![/bold green]")
        else:
            console.print(f"[bold red]Failed:[/bold red] {response.text}")

    def deleteBookById(self):
        pub_id = Prompt.ask("What is the ID?")
        response = self.req_book.delete(int(pub_id))

        if response.status_code == 200:
            console.print(response.json())
        else:
            console.print("[red]Not found.[/red]")

    def deleteMagazineById(self):
        pub_id = Prompt.ask("ID: ")
        response = self.req_magazine.delete(int(pub_id))

        if response.status_code == 200:
            console.print("Deleted with success", response.json())
        else:
            console.print("[red]Not found.[/red]")

    def deleteCollection(self):
        pass

    def updatePatch(self):
        console.print("[bold blue]--- Update publication ---[/bold blue]")

        table_name = Prompt.ask("Book or Magazine").lower()
        id_pub = Prompt.ask("ID of the publication to update")

        response = self.ViewUtils.selectPublicationTypeAndId(table_name, id_pub)

        if response and response.status_code == 200:
            data = response.json()

            # If the response is a dict, convert it to a list
            if isinstance(data, dict):
                data = [data]

            table = Table(title=f"Updating {table_name.capitalize()} details")

            table.add_column("Field", justify="center", style="cyan", no_wrap=True)
            table.add_column("Current Value", style="magenta")
            table.add_column("New Value", style="green")

            current_values = {
                "Title": data[0].get("title", "Not Found"),
                "Author": data[0].get("author", "Unknown"),
                "Year": data[0].get("year", "-"),
                "Pages": data[0].get("pages_number", "0"),
                "Genre": data[0].get("genre", "Unknown"),
                "Rating": data[0].get("avaliation", "0"),
            }

            for field, value in current_values.items():
                new_value = Prompt.ask(
                    f"New value for {field} (leave empty to keep the current value): ",
                    default=value,
                )                
                if new_value:
                    table.add_row(field, value, new_value)
                else:
                    table.add_row(field, value, value) # Value = not modified value

            console.print(table)

            confirm = " "

            while (confirm != "yes" or confirm != "no"):
                confirm = Prompt.ask(
                    "Do you want to update this publication? (yes/no)", choices=["yes", "no"]
                )
                if confirm == "yes" or confirm == "y":
                    confirm = "yes"
                    updated_data = {
                        field.lower(): new_value if new_value else value
                        for field, value, new_value in zip(
                            current_values.keys(),
                            current_values.values(),
                            table.columns[2].cells
                        )
                    }

                    # Remove the 'Field' column (first column)
                    updated_data.pop("field", None)

                    # Send the updated data back to the server
                    if table_name == "book":
                        response = self.req_book.update(id_pub, updated_data)
                    elif table_name == "magazine":
                        response = self.req_magazine.update(id_pub, updated_data)

                    if response.status_code == 200:
                        console.print(
                            f"[bold green]Successfully updated the {table_name}[/bold green]"
                        )
                    else:
                        console.print(
                            f"[red]Error while updating: {response.status_code}[/red]"
                        )

                elif confirm == "no" or confirm == "n":
                    console.print("[yellow]Update cancelled.[/yellow]")
                else:
                    console.print("[blue]Select 'yes' or 'no'[/blue]")

        else:
            code = response.status_code if response else "Error"
            console.print(f"[red]Error:[/red] {code}")

    def filters(self):
        pass

    def filterByWord(self):
        pub_type = Prompt.ask("Filter by (Book or Magazine): ").lower().strip()
        pub_word = Prompt.ask("Search word: ").lower().strip()
        pub_column = Prompt.ask("What column: ").lower().strip()

        # Validade table exists
        if pub_type == "book" or pub_type == "books":
            table_name = "books"
            response = self.req_book.getByWord(pub_column, pub_word)
        elif pub_type == "magazine" or pub_type == "magazines":
            table_name = "magazines"
            response = self.req_magazine.getByWord(pub_column, pub_word)
        else:
            console.print(
                f"[red]Invalid publication type '{pub_type}'. Choose 'Book' or 'Magazine'.[/red]"
            )
            return

        # Validate column exists
        column_names = utils.getTableNames(table_name)

        if not column_names or pub_column not in column_names:
            console.print(
                f"[red]Column '{pub_column}' not found in table '{table_name}'.[/red]\n"
                f"[yellow]Available columns:[/yellow] {column_names}"
            )
            return

        if response.status_code != 200:
            console.print(f"[red]Error: {response.status_code} - {response.text}[/red]")
            return

        data = response.json()

        if not data:
            console.print("[yellow]No results found.[/yellow]")
            return

        # Convert dict to list, for best data manipulation
        if isinstance(data, dict):
            data = [data]

        console.print(f"[bold green]Found {len(data)} result(s):[/bold green]")

        for item in data:
            console.print(item)

from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from program.View.Requests import HttpRequest

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

        if table_name == "book":
            response = self.req_book.getAll()
        elif table_name == "magazine":
            response = self.req_magazine.getAll()
        else:
            console.print(f"[red]Table '{table_name}' don't exist[/red]")
            return

        if response.status_code == 200:
            data = response.json()
            
            # Create a table uwu
            table = Table(title="All publications")

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

        # Corrigindo input (adicionado parenteses no lower)
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

            # --- CORREÇÃO 1: Garantir que é uma lista para o loop funcionar ---
            # Se a API retornou um único dicionário, transformamos em lista com 1 item
            if isinstance(data, dict):
                data = [data]

            table = Table(title=f"{table_name.capitalize()} details")

            # Colunas Padrão
            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("Title", style="magenta")
            table.add_column("Author", style="green")
            table.add_column("Year", justify="center")
            table.add_column("Pages", justify="center")
            table.add_column("Genre", justify="center")
            table.add_column("Rating", justify="center")
            
            # Adiciona coluna extra no cabeçalho se for revista
            if table_name == "magazine":
                table.add_column("Edition", justify="center", style="yellow")

            for item in data:
                # --- CORREÇÃO 2: Montar a linha em uma lista antes de adicionar ---
                
                # 1. Cria a lista com os dados comuns
                row_data = [
                    str(item.get("id", "-")),
                    item.get("title", "Not Found"),
                    item.get("author", "Unknown"),
                    str(item.get("year", "-")),
                    str(item.get("pages_number", "0")),
                    str(item.get("genre", "Unknown")),
                    str(item.get("avaliation", "0"))
                ]

                # 2. Se for revista, adiciona o dado extra nessa mesma lista
                if table_name == "magazine":
                    # Certifique-se que sua API retorna a chave "edition" ou "edicao"
                    row_data.append(str(item.get("edition", "-")))

                # 3. Usa o asterisco (*) para "desempacotar" a lista como argumentos
                table.add_row(*row_data)

            # Para visualizar item único, print direto é melhor que pager
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

    def update(self):
        pass

    def updateUserConfiguration(self):
        pass

    def filters(self):
        pass

    def filterByWord(self):
        pub_word = Prompt.ask("search: ")
        response = self.req_magazine.getByVariable(str(pub_word))

        if response.status_code == 200:
            console.print(response.json())
        else:
            console.print("[red]Not found.[/red]")

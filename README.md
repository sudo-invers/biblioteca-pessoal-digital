# biblioteca-pessoal-digital


# Objetivo:

Desenvolver um sistema de linha de comando (CLI), para gerenciar uma biblioteca pessoal de livros e revistas digitais, 
permitindo o cadastro de publicações, o registro de leituras, o controle de status (lido/ não lido/ em leitura) e a geração de relatórios sobre o acervo.
O sistema deve aplicar conceitos de encapsulamento, herança (simples e múltipla), métodos especiais, regras de negócio configuráveis.
A persistência pode ser feita em JSON ou SQLite, com um repositório desacoplado do domínio.


# Estrutura das Classes:

```mermaid

classDiagram
    %%the '&#10240', is for the 1..* not overlapping the arrow
    Publication "&#10240 &#10240 &#10240 &#10240 &#10240 &#10240 1..*"   <|-- "1" Book
    Publication "1"         <|-- "1" Magazine
    Repository              <|-- PublicationRepository 

    Publication "1..1"      --> "0..*" Anotation
    Publication             --> PublicationType : type
    Publication             --> ReadingStatus
    PublicationService      --> PublicationRepository 
    PublicationController   --> PublicationService
    ReadingStatus           --> AlterStatus
    Repository              --> RepositoryConnection
    CLI                     --> PublicationController : use
    CLI                     --> CommandParser : interprateCommands
    CLI                     --> Menu : list options

    Collection  "1..1"      *-- "0..*" Publication

    Menu --> Command : the cli commmands
    CommandParser --> Command : convert text to commands

    class Publication{
        <<abstract>>
        -Long id
        -String title
        -String author
        -int year
        -Date inclusionDate
        -int pagesNumber
        -int avaliation
        -String genre
        -List<Anotation> anotations
        -ReadingStatus status
        -PublicationType type

    }
    class PublicationType{
        <<enumeration>>
        BOOK
        MAGAZINE
    }
    class ReadingStatus{
        -AlterStatus status
        -Date startedDate
        -Date completedDate
        -Date startReading 
        -Date finishReading

        +markAsReading()
        +markAsRead()
    }
    class AlterStatus{
        <<enumeration>>
        UNREAD
        READING
        READ
    }
    class Book{
    }
    class Magazine{
    }
    class Anotation{
        -Long id
        -String name
        -Date date
        -String passage
        -String description
    }
    class Report{
        +unreadAmount() int
        +readingAmount() int
        +readAmount() int
        +publicationAmount() int
        +getReadAverageScore() float
        +bestFive() List~String~

    }
    class Settings{
        <<Settings.json>>
        favoriteGenre
        simultaneousPageLimit
        annualReadingTarget
    }
    class RepositoryConnection {
        +execute()
        +executeMany()
    }
    class Repository {
        -RepositoryConnection connection

        +save(Object)
        +getAll(Object)
        +getById(Long id)
        +updateById(Long id)
        +deleteById(Long id)
        +searchByWord(String word)
    }
    class PublicationRepository{

        +createPublication(Publication)
        +createAnotation(Long publicationId, Anotation anotation) save()
        +getAllPublications() getAll()
        +getPublicationById(Long id) getById()
        +getPublicationByTitle(String title) searchByWord()
        +getPublicationByAuthor(String author) searchByWord()
        +getPublicationByGenre(String genre) searchByWord()

        +updatePublicationById(int id) updateById()
        +deletePublicationById(int id) deleteById()
    }
    class PublicationService{
        %%makes the business rules
        -PublicationRepository repo

        +createPublication(Publication)
        +createAnotation(Long PublicationId, Anotation anotation )

        +getAllPublications()
        +getPublicationById(Long id)
        +getPublicationByTitle(String title)
        +getPublicationByAuthor(String author)
        +getPublicationByGenre(String genre)

        +updatePublicationById(Long id)
        +deletePublicationById(Long id)

        +startReading(Long id)
        +finishReading(Long id)
        +evaluate(Long id, int score)

        +validateReadingSequence(ReadingStatus status)
        +validateEvaluation(Publication publication)
        +checkSimultaneousReadingLimit()

    }
    class PublicationController{
        %%receives and sends requests

        +createPublication(Publication publication) Publication
        +createAnotation(Long publicationId, Anotation anotation) Anotation

        +getAllPublications() List~Publication~
        +getPublicationById(Long id) Publication
        +getPublicationByTitle(String title) List~Publication~
        +getPublicationByAuthor(String author) List~Publication~
        +getPublicationByGenre(String genre) List~Publication~

        +updatePublicationById(Long id, Publication publication)
        +deletePublicationById(Long id)
    }
    class Collection{
        -List<Publication> publications
    }
    %%----------------------Command line interface--------------------%%
        class CLI {
        +start()
        +readInput() String
        +executeCommand(String)
        +printResult(Object)
    }

    class Menu {
        +showMainMenu()
        +showPublicationMenu()
        +listOptions()
    }

    class CommandParser {
        +parse(String input) Command
    }
%%(bib cadastrar, bib listar, bib anotar, bib relatorio
    class Command {
        <<enumeration>>
        CREATE_PUBLICATION
        LIST_PUBLICATIONS
        FIND_BY_ID
        FIND_BY_TITLE
        FIND_BY_AUTHOR
        UPDATE_PUBLICATION
        DELETE_PUBLICATION
        CREATE_ANOTATION
        EXIT
    }


```

# Estrutura planejada de classes
```bash
.
├── main.py
├── program
│   ├── cli
│   │   ├── CLI.py
│   │   ├── ComandParser.py
│   │   ├── Comands.py
│   │   ├── Menu.py
│   │   └── window.txt
│   ├── controller
│   │   └── PublicationController.py
│   ├── domain
│   │   ├── AlterStatus.py
│   │   ├── Anotation.py
│   │   ├── Book.py
│   │   ├── Colletion.py
│   │   ├── Magazine.py
│   │   ├── Publication.py
│   │   ├── PublicationType.py
│   │   ├── ReadingStatus.py
│   │   └── Report.py
│   ├── repository
│   │   ├── RepositoryConnection.py
│   │   └── Repository.py
│   ├── service
│   │   └── PublicationService.py
│   └── settings.json
├── README.md
└── venv
```

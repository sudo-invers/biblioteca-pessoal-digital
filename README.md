# biblioteca-pessoal-digital


# Objetivo:

Desenvolver um sistema de linha de comando (CLI), para gerenciar uma biblioteca pessoal de livros e revistas digitais, 
permitindo o cadastro de publicações, o registro de leituras, o controle de status (lido/ não lido/ em leitura) e a geração de relatórios sobre o acervo.
O sistema deve aplicar conceitos de encapsulamento, herança (simples e múltipla), métodos especiais, regras de negócio configuráveis.
A persistência pode ser feita em JSON ou SQLite, com um repositório desacoplado do domínio.


# Estrutura das Classes:

<img width="2166" height="2608" alt="Untitled diagram-2025-11-18-152217" src="https://github.com/user-attachments/assets/828af2cf-074c-4693-814c-54b36f58c71e" />

# Estrutura planejada de classes
```bash
.
├── main.py
├── program
│   ├── controller
│   │   ├── BookController.py
│   │   ├── MagazineController.py
│   │   └── ObraController.py
│   ├── model
│   │   ├── Book.py
│   │   ├── Magazine.py
│   │   └── Obra.py
│   ├── repository
│   │   ├── RepositoryConnection.py
│   │   └── Repository.py
│   └── service
│       ├── BookService.py
│       ├── MagazineService.py
│       └── ObraService.py
└── README.md
```

from abc import ABC
import sqlite3
from zipapp import create_archive


"""

def procurar_biblioteca_db(diretorio_inicial):
    # Subindo um nível (diretório para trás) em relação ao diretório inicial
    diretorio_inicial = os.path.abspath(os.path.join(diretorio_inicial, '..'))

    # Percorrendo todos os diretórios a partir do diretório "diretorio_inicial"
    for root, dirs, files in os.walk(diretorio_inicial):
        if 'biblioteca.db' in files:
            return root  # Retorna o diretório onde o arquivo foi encontrado
    
    return None  # Retorna None se o arquivo não for encontrado

# Exemplo de uso
diretorio_encontrado = procurar_biblioteca_db('/caminho/para/o/diretorio')
if diretorio_encontrado:
    print(f"Arquivo 'biblioteca.db' encontrado em: {diretorio_encontrado}")
else:
    print("Arquivo 'biblioteca.db' não encontrado.")

"""

class RepositoryConnection(ABC):

    def __init__(self, query):
        self._query = query

    def novaQuery(query):
        # Verify if the bookshelf.db exists, if don't, create it;
        try:
            dbLocation = "/databases/bookshelf.db"
            
            if (not dbLocation.exists):
                # Creating the file;
                create_archive(dbLocation)
                # if cannot be created;
                if (not dbLocation.exists):
                    return FileNotFoundError(f"File '{dbLocation}' not found")
            

            # Conecta ao sqlite3;
            connection = sqlite3.connect("bookshelf.db")
            cursor = connection.cursor()
            print("DB Init")

            # Executa a query
            cursor.execute(query)

            cursor.close()


        except sqlite3.Error as error:
            # se acontecer algum error, ele retorna ao ultimo ponto de commit;
            print(f"error - {error} fazendo rollback")
            cursor.rollback()
        finally:
            # close the  sqlite and commit the channges (if not in rollback);
            if connection:
                connection.commit()
                connection.close()
                print("sucesso")
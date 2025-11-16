from abc import ABC, abstractmethod
import sqlite3


class Connection(ABC):

    def __init__(self, query):
        self._query = query

    @abstractmethod
    def novaQuery(query):
        try:

            #cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,));

            # Conecta ao sqlite3;
            connection = sqlite3.connect('biblioteca.db')
            cursor = connection.cursor()
            print("DB Init")

            # Executa a query
            cursor.execute(query)

            cursor.close()


        except sqlite3.Error as error:
            # se acontecer algum error, ele retorna ao ultimo ponto de commit;
            print("error -", error, "fazendo rollback")
            cursor.rollback()
        finally:
            # fecha o sqlite
            if connection:
                connection.commit()
                connection.close()
                print("sucesso")
from program.model import Obra

class Livro(Obra):
    def __init__(self, id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao, numeroPaginas):
        super().__init__(id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)
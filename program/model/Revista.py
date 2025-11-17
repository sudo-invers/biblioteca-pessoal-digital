from program.model import Obra

class Revista(Obra):
    def __init__(self, id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao, edicao):
        super().__init__(id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)

        self._edicao = edicao

    
    
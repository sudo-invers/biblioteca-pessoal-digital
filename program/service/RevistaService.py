from program.model import Obra
from program.repository import Repository as repo
from ObraService import ObraService

@property
class ObraService(ObraService, Obra):
    
    # Chama o construtor da classe base 'Obra' para inicializar os atributos;
    def __init__(self, id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao, edicao):
        super().__init__(id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)
        
        self._edicao = edicao

    def getByEdicao():
        return repo.getByEdicao


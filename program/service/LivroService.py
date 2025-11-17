from program.model import Obra
from ObraService import ObraService


@property
class ObraService(ObraService, Obra):
    
    # Chama o construtor da classe base 'Obra' para inicializar os atributos;
    def __init__(self, id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao, edicao):
        super().__init__(id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)

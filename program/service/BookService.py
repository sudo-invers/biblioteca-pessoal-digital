from program.model import Obra
from ObraService import ObraService


@property
class BookService(ObraService, Obra):
    
    # Call the constructor from 'Obra' to initialize the atributes;
    def __init__(self, id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao):
        super().__init__(id, titulo, autor, ano, tipo, genero, quantidade_paginas, status, avaliacao, anotacao)

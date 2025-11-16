from abc import ABC


@property
class Obra(ABC):
    """
    classe abstrata que ira vai ser implementada em Livro.py e Revista.py
    Originalmente, publicação
    """

    def __init__(self, id, titulo, autor, ano, tipo, genero, quantidadePaginas, status, avaliacao, anotacao):
        self._id                 = id
        self._titulo             = titulo
        self._autor              = autor
        self._ano                = ano
        self._tipo               = tipo      # [livro ou revista]
        self._genero             = genero
        self._quantidadePaginas  = quantidadePaginas
        self._status             = status    # [naoLido, lido, lendo]
        self._avaliacao          = avaliacao # [0 _ 10(opcional)]
        self._anotacao           = anotacao  # [data e trecho]

    
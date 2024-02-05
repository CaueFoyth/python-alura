from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Obriga a classes filhas ter esse método
    @abstractmethod
    def aplicar_desconto(self):
        pass
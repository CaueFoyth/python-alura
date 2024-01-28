class Restaurante:
    restaurantes = []

    #Construtor
    def __init__(self, nome, categoria):
        self._nome = nome.title() #.title() Capitaliza a string
        self._categoria = categoria.upper() #.upper() Deixa tudo em caixa alta

        # _ Para não ser acessado direto, só por método para alterar
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # Método da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    # Alterar a vizualização do restaurante.ativo
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

# Criando os restaurantes com o objeto
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
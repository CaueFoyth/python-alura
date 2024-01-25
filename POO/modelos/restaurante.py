class Restaurante:
    restaurantes = []

    #Construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

        # _ Para não ser acessado direto, só por método para alterar
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    # Alterar a vizualização do restaurante.ativo
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

# Criando os restaurantes com o objeto
restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
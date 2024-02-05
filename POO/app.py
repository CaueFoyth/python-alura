from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avalicao('Gui', 3)
restaurante_praca.receber_avalicao('Lais', 4)
restaurante_praca.receber_avalicao('Caue', 5)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_mexicano.receber_avalicao('Caue', 5)

# restaurante_japones = Restaurante('Japa', 'Japonesa')
# # restaurante_japones.receber_avalicao('Caue', 8)

# restaurante_mexicano.alternar_estado()

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_pao = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
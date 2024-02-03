from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avalicao('Gui', 10)
restaurante_praca.receber_avalicao('Lais', 8)
restaurante_praca.receber_avalicao('Caue', 5)

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avalicao('Caue', 7)

restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avalicao('Caue', 8)

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
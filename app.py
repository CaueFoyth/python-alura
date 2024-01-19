import os

def exibir_nome_prgrama(): 
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair")

def finaliza_app():
    os.system("cls")
    print("Encerrando o programa...\n")

def escolher_opcao():
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            finaliza_app()
        case _:
            print('Opção inválida!')


def main():
    exibir_nome_prgrama()
    exibir_opcoes()
    escolher_opcao()

# Arquivo principal do prgrama
if __name__ == '__main__':
    main()
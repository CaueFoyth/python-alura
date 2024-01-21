import os

restaurantes = ["Pizza", "Sushi"]

def exibir_nome_prgrama(): 
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair")

def finaliza_app():
    exibir_subtitulos("Encerrando o programa...")

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()

def opcao_invalida():
    exibir_subtitulos("Opção inválida!")
    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")

    # Colocar o nome do restaurante na lista
    restaurantes.append(nome_restaurante)

    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos("Restaurantes cadastrados")

    for restaurante in restaurantes:
        print(f"- {restaurante}")

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finaliza_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_prgrama()
    exibir_opcoes()
    escolher_opcao()

# Arquivo principal do prgrama
if __name__ == '__main__':
    main()
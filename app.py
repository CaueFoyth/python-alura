import os

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False}, 
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiana", "ativo":False}]

def exibir_nome_prgrama(): 
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar estado do restaurante")
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
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome":nome_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_restaurante)

    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos("Restaurantes cadastrados")

    # ljust serve para definir espaços no terminal
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]

        # if ternário
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"

        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def estado_restaurante():
    exibir_subtitulos("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True

            # Inverter de True para False ou False para True 
            restaurante["ativo"] = not restaurante["ativo"]
            
            # Ternário
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

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
                estado_restaurante()
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
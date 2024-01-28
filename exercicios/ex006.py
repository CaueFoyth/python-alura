# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista = [6, 7, 8]
i = 0
try:
    for numero in lista:
        i = i + 1
    print(f"A média do valores da lista é {sum(lista)/i}")

except:
    print("Ocorreu algum erro!")
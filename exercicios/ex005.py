# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista = [1, 3, 5, 10]

try:
    print(sum(lista))
except:
    print("Ocorreu um erro!")
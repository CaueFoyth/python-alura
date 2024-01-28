# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input("Insira um número para se obter a tabuada: "))

for i in range(10):
    i = i + 1
    print(f"{numero} x {i} = {numero*i}")
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

x = []
for i in range(10):
    i = i + 1
    x.append(i)

x.reverse()
print(x)
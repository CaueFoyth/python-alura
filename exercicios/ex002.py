# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

x = []

for i in range(10):
    i = i + 1
    if i % 2 == 1:
        x.append(i)

print(sum(x))
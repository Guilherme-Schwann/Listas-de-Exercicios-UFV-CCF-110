soma = 0
cont = 1
for i in range(37, 0, -1):
    soma += i * (i + 1) / cont
    cont += 1
print(soma)
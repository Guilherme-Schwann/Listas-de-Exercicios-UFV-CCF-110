X = int(input())
cont = 1
soma = 0
for i in range(25, 0, -1):
    if cont % 2 == 1:
        soma += pow(X, i) / cont
    else:
        soma -= pow(X, i) / cont
    cont += 1
print(soma)
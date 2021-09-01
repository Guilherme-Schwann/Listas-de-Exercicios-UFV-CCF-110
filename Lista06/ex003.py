v1 = [0 for x in range(20)]
v2 = [0 for x in range(20)]
cont = 19
for i in range(20):
    v1[i] = int(input('Insira um valor: '))
for i in range(20):
    print(v1[i], end=' ')
    v2[cont] = v1[i]
    cont -= 1
print()
for i in range(20):
    print(v2[i], end=' ')

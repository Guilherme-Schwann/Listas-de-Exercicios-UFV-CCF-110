n = int(input('Tamanho do vetor: '))
v = [int((input())) for x in range(n)]
v2 = []
v2quant = []
for i in range(n):
    for j in range(n-1):
        if v[j] > v[j+1]:
            temp = v[j]
            v[j] = v[j+1]
            v[j+1] = temp
print(v)
check = 0
for i in range(n):
    if v[i] == v[i - 1] and check == 1:
        v2quant[-1] += 1
    elif v[i] == v[i-1] and check == 0:
        v2.append(v[i])
        v2quant.append(2)
        check = 1
    else:
        check = 0
for i in range(len(v2)):
    print(f'Número {v2[i]} repetido {v2quant[i]} vezes.')

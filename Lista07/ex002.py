v = [int(input()) for x in range(20)]
maior, menor = v[0], v[0]
for i in range(20):
    if v[i] < menor:
        menor = v[i]
    elif v[i] > maior:
        maior = v[i]
print(f'Menor: {menor}\nMaior: {maior}')

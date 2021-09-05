v = [int(input()) for x in range(121)]
menor, maior = v[0], v[0]
soma = 0
for i in range(121):
    soma += v[i]
media = soma / 121
diasmen = 0
for i in range(121):
    if v[i] < menor:
        menor = v[i]
    elif v[i] > maior:
        maior = v[i]
    if v[i] < media:
        diasmen += 1
print(f'Menor temp.: {menor} | Maior temp.: {maior}')
print(f'Média de temperatura: {media}')
print(f'Foram {diasmen} dias com a temperatura menor que a média.')

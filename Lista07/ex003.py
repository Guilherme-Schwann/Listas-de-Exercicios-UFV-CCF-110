v = [int(input()) for x in range(5)]
maior, menor = v[0], v[0]
ima, ime = 0, 0
for i in range(5):
    if v[i] > maior:
        maior = v[i]
        ima = i
    elif v[i] < menor:
        menor = v[i]
        ime = i
print(f'Maior: {maior} / Índice: {ima}')
print(f'Menor: {menor} / Índice: {ime}')
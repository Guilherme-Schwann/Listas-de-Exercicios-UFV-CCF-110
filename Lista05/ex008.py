maior = int(input())
menor = maior
if maior == -1:
    print('Nenhum valor inserido.')
else:
    while True:
        num = int(input())
        if num == -1:
            break
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    print(f'Maior: {maior}, Menor: {menor}')
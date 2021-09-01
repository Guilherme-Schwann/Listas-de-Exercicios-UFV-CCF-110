quant = int(input('Quantos números serão inseridos? '))
maior = int(input())
for i in range(quant - 1):
    num = int(input())
    if num > maior:
        maior = num
print(f'Maior: {maior}')
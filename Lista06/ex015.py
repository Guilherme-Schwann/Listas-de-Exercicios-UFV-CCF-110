quant = int(input('Quantidade de caixas: '))
pesot = 0
precot = 0
for i in range(quant):
    peso = float(input(f'Peso da caixa {i + 1}: '))
    pesot += peso
    preco = float(input(f'Preço da caixa {i + 1}: '))
    precot += preco
valor = float(input('Valor total da carga: '))
print(f'Peso total: {pesot}')
print(f'Valor total: {precot}')
if precot != valor:
    print('Há diferença entre o preço total calculado e o valor inserido!')

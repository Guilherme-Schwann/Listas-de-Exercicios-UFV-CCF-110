nome = input('Seu nome: ')
num = int(input('Número de carros vendidos: '))
total = float(500)
for i in range(num):
    val = float(input(f'Valor da {i + 1}° venda: '))
    total += val * 0.05
    total += 50
print(f'O salário de {nome} é igual a R${total:.2f}')
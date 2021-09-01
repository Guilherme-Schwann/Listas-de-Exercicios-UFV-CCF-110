total = 0
while True:
    num = int(input('Número do pedido: '))
    if num == 0:
        break
    data = input('Data do pedido DD/MM/AA: ')
    pruni = float(input('Preço unitário: '))
    quant = int(input('Quantidade: '))
    total += pruni * quant
print(f'Total: R${total:.2f}')
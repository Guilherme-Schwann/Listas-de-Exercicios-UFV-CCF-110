despesa = float(input('Insira o valor gasto: R$'))
gorjeta = (despesa * 10) / 100
total = despesa + gorjeta
print(f'O valor da gorjeta é R${gorjeta:.2f}')
print(f'O valor total com a gorjeta é R${total:.2f}')

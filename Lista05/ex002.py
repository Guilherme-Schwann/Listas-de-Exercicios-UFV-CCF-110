saldo = float(input('Insira seu saldo médio do último ano: '))
if 0 < saldo <= 500:
    print(f'Saldo médio: {saldo:.2f}\nCrédito: Nenhum crédito.')
    exit()
elif 501 < saldo <= 1000:
    cred = (30 / 100) * saldo
elif 1001 < saldo <= 3000:
    cred = (40 / 100) * saldo
elif 3001 <= saldo:
    cred = (50 / 100) * saldo
cred += cred * (2/100)
print(f'Saldo médio: {saldo:.2f}\nCrédito: {cred:.2f}')

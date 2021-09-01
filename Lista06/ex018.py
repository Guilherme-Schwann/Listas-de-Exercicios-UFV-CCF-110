conta = []
saldo = []
totaln = 0
total = 0
salt = 0
while True:
    con = int(input('Conta: '))
    if con < 0:
        break
    sal = float(input('Saldo: '))
    conta.append(con)
    saldo.append(sal)
    total += 1
    salt += sal
qua = len(conta)
for i in range(qua):
    print(f'Conta: {conta[i]} / Saldo: {saldo[i]}')
    if saldo[i] < 0:
        print('Negativo')
        totaln += 1
    else:
        print('Positivo')
print(f'Clientes negativos: {totaln}')
print(f'Total de clientes: {total}')
print(f'Saldo da agência: {salt}')
print(f'{100 * totaln / total}% de contas negativas.')

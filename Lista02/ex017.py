salario = float(input('Insira seu salário: R$'))
credito = float(input('Insira o valor da prestação de crédito: R$'))
porcentagem = salario * 0.3
if credito <= porcentagem:
    print('O empréstimo pode ser concedido.')
else:
    print('O empréstimo não pode ser concedido.')

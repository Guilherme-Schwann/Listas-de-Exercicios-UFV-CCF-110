mes = int(input('Insira um número correspondente a um mês do ano: '))
if 0 < mes <= 3:
    print('1° trimestre.')
elif 3 < mes <= 6:
    print('2° trimestre.')
elif 6 < mes <= 9:
    print('3° trimestre.')
elif 9 < mes <= 12:
    print('4° trimestre.')
else:
    print('Mês inválido.')

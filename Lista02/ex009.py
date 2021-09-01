A = int(input('Insira um número: '))
B = int(input('Insira outro número: '))
if B == 0:
    print('Divisão impossível')
    exit()
resto = A % B
if resto == 0:
    print(f'{A} é divisível por {B}')
else:
    print(f'{A} não é divisível por {B}')

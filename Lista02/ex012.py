import math
num = int(input('Insira um número: '))
if num >= 0:
    print(f'A raiz quadrada de {num} é {math.sqrt(num)}.')
else:
    print(f'O valor de {num} elevado ao quadrado é de {pow(num, 2)}')

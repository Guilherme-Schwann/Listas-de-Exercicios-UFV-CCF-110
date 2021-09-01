import math
#Ex.20
x = int(input())
y = int(input())
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
menor = pow(menor, 2)
try:
    maior = math.sqrt(maior)
except:
    maior = str('Não foi possível calcular a raiz do maior número.')
print(f'{menor}\n{maior}')

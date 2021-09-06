m = [[int(input()) for i in range(7)] for j in range(7)]
N = int(input('Qual o valor procurado? '))
check = 0
for i in range(7):
    for j in range(7):
        if N == m[i][j]:
            check = 1
            print(f'O número {N} se encontra na linha {i+1}, coluna {j+1}.')
if check == 0:
    print('Número não encontrado.')
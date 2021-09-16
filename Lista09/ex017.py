C, D = int(input('Número de linhas da Matriz A: ')), int(input('Número de colunas da Matriz A: '))
E, F = int(input('Número de linhas da Matriz B: ')), int(input('Número de colunas da Matriz B: '))
if D != E:
    print('Multiplicação de A por B impossível.')
    exit()
A = [[int(input('Matriz A: ')) for i in range(D)] for j in range(C)]
B = [[int(input('Matriz B: ')) for i in range(F)] for j in range(E)]
res = [[0 for i in range(F)] for j in range(C)]
for i in range(C):
    for j in range(F):
        for k in range(D):
            res[i][j] += A[i][k] * B[k][j]
for i in range(C):
    print(res[i])

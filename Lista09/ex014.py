N = int(input('Ordem da matriz: '))
A = [[int(input()) for i in range(N)] for j in range(N)]
check = 0
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            check += 1
if check == 0:
    print('A matriz é simétrica.')
else:
    print('A matriz não é simétrica.')

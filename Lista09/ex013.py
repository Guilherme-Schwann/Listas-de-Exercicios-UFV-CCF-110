N = int(input('Ordem da matriz: '))
A = [[int(input()) for i in range(N)] for j in range(N)]
At = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        At[i][j] = A[j][i]
for i in range(N):
    print(At[i])

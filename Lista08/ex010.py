A = [[int(input()) for i in range(4)] for j in range(4)]
B = [[int(input()) for i in range(4)] for j in range(4)]
SOMA = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    for j in range(4):
        SOMA[i][j] = A[i][j] + B[i][j]
print(SOMA)

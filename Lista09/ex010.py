M = [[int(input()) for i in range(3)] for j in range(3)]
M2 = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        M2[i][j] = M[2-i][2-j]
for i in range(3):
    print(M2[i])

m = [[int(input()) for i in range(5)] for j in range(4)]
soma = 0
for i in range(4):
    for j in range(5):
        soma += m[i][j]
print(soma)

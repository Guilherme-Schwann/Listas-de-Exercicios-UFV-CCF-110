m = [[int(input()) for i in range(10)] for j in range(10)]
soma = 0
for i in range(10):
    for j in range(10):
        if j > i:
            soma += m[i][j]
print(soma)
m = [[int(input()) for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        if i + j == 9:
            print(m[i][j], end=' ')

a = [[int(input('1° matriz: ')) for i in range(5)] for j in range(5)]
b = [[int(input('° matriz: ')) for i in range(5)] for j in range(5)]
dif = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        dif[i][j] = a[i][j] - b[i][j]
print(dif)

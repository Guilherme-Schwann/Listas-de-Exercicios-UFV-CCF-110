m = [[int(input()) for i in range(2)] for j in range(2)]
for i in range(2):
    for j in range(2):
        if m[i][j] % 2 == 1:
            m[i][j] *= 2
print(m)
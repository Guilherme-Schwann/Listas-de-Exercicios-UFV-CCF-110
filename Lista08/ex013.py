A = [[int(input()) for i in range(5)] for j in range(3)]
sl = [0 for i in range(3)]
for i in range(3):
    for j in range(5):
        sl[i] += A[i][j]
print(sl)

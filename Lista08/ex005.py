m = [[int(input()) for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        if j > i:
            print(m[i][j])
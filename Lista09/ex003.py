m = [[int(input()) for i in range(10)] for j in range(10)]
prod = 1
for i in range(10):
    for j in range(10):
        if i > j:
            prod *= m[i][j]
print(prod)

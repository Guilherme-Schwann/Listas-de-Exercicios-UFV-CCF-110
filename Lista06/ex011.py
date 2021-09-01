v = [0 for x in range(15)]
for i in range(15):
    v[i] = int(input())
    if v[i] < 0:
        v[i] = -1
    else:
        v[i] = v[i] ** (1/2)
for i in range(15):
    print(v[i])
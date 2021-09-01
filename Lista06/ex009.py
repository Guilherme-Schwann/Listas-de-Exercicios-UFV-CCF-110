v1 = [0 for x in range(5)]
v2 = [0 for x in range(5)]
v3 = [0 for x in range(5)]
for i in range(5):
    print(f'{i + 1}° soma: ')
    v1[i] = int(input())
    v2[i] = int(input())
    v3[i] = v1[i] + v2[i]
for i in range(5):
    print(v3[i], end=' ')

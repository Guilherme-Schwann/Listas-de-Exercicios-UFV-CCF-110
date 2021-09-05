N = int(input('Tamanho do vetor: '))
v = [int(input()) for x in range(N)]
v2 = v
for i in range(N):
    for j in range(N-1):
        if v2[j] > v2[j+1]:
            temp = v2[j]
            v2[j] = v2[j+1]
            v2[j+1] = temp
print(v2)
for i in range(N):
    for y in range(N-1):
        if v2[y] < v2[y+1]:
            temp = v2[y]
            v2[y] = v2[y+1]
            v2[y + 1] = temp
print(v2)

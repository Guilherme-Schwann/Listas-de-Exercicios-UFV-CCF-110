n = int(input('Tamanho do vetor: '))
v = [0 for x in range(n)]
sum = 0
for i in range(n):
    v[i] = int(input())
    if i % 2 == 0:
        sum += v[i]
print(sum)
N = int(input('Número de pessoas: '))
v = []
soma = 0
for i in range(N):
    v.append(float(input(f'Renda da pessoa {i+1}: ')))
    soma += v[i]
media = soma / N
for i in range(N):
    for j in range(N-1):
        if v[j] > v[j+1]:
            temp = v[j]
            v[j] = v[j+1]
            v[j+1] = temp
if N % 2 == 0:
    mediana = (v[int(N / 2)] + v[int((N / 2) - 1)]) / 2
else:
    mediana = v[int(N / 2)]
print(f'Média das rendas: {media:.2f}')
print(f'Mediana das rendas: {mediana:.2f}')

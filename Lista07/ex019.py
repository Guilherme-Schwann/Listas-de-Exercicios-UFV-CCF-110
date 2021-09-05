N = int(input('Comprimento do vetor: '))
v = [int(input(f'{x+1}° valor: ')) for x in range(N)]
k = int(input('Qual posição você quer saber? '))
print(v)
print(f'O {k}° termo do vetor (antes da ordenação) é: {v[k-1]}')
for i in range(N):
    for j in range(N-1):
        if v[j] > v[j+1]:
            temp = v[j]
            v[j] = v[j+1]
            v[j+1] = temp
print(v)
print(f'O {k}° termo do vetor (depois da ordenação) é: {v[k-1]}')

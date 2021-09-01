v = [int(input()) for x in range(10)]
soma = 0
for i in range(10):
    print(v[i], end=' ')
    soma += v[i]
print(f'\nMédia: {soma/10}')
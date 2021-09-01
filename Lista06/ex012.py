v = [0 for x in range(10)]
soma = 0
for i in range(10):
    v[i] = float(input())
    soma += v[i]
media = soma / 10
for i in range(10):
    if v[i] > media:
        print(v[i])
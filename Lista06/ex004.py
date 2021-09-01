v = []
check = 0
for i in range(25):
    x = int(input())
    v.append(x)
n = int(input('Qual número procuras? '))
for i in range(25):
    if v[i] == n:
        check += 1
        print(i, end=' ')
if check == 0:
    print(f'Erro, número {n} não foi encontrado.')

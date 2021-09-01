A1 = int(input())
A2 = int(input())
N = int(input())
if N < 3:
    print('Número de termos insuficiente para formar uma sequência.')
    exit()
for i in range(N):
    i += 3
    if i % 2 == 0:
        A3 = A2 - A1
    else:
        A3 = A2 + A1
    print(A1, end=' ')
    A1 = A2
    A2 = A3

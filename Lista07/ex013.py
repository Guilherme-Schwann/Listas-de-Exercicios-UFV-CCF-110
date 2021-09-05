A = []
for i in range(30):
    check, check2 = 0, 0
    while check != 1:
        n = int(input(f'{i+1}° Termo (1° vetor): '))
        for j in range(len(A)):
            if n == A[j]:
                check2 = 1
        if check2 == 0:
            check = 1
        else:
            check2 = 0
    A.append(n)
B = [int(input(f'{x}° Termo (2° vetor): ')) for x in range(30)]
X = int(input('Número para busca: '))
for i in range(30):
    if X == A[i]:
        print(B[i])

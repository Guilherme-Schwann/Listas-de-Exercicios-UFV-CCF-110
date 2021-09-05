n = int(input('Insira o tamanho da lista: '))
A = [int(input(f'{x + 1}° termo: ')) for x in range(n)]
A2 = []
rep = []
repind = []
repquant = []
check, check2 = 0, 0
for i in range(n):
    for j in range(len(A2)):
            if A2[j] == A[i]:
                check2 = 1
                for k in range(len(rep)):
                    if A2[j] == rep[k]:
                        repquant[k] += 1
                        check = 1
                if check == 0:
                    rep.append(A[i])
                    repind.append(i)
                    repquant.append(2)
                else:
                    check = 0
    if check2 == 0:
        A2.append(A[i])
    else:
        check2 = 0
for i in range(len(rep)):
    print(f'Número repetido: {rep[i]}')
    print(f'Repetido {repquant[i]} vezes.')
print(A2)

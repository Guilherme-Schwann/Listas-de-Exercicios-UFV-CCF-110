tam = int(input('Tamanho dos vetores: '))
v1 = [int(input('Vetor 1: ')) for x in range(tam)]
v2 = [int(input('Vetor 2: ')) for x in range(tam)]
v3 = [0 for x in range(tam * 2)]
for i in range(tam * 2):
    if i % 2 == 0:
        v3[i] = v1[int(i / 2)]
    else:
        v3[i] = v2[int(i / 2)]
    print(v3[i])
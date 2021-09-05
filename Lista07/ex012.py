nota = [float(input()) for x in range(80)]
nota2 = []
freq_abs = []
freq_rel = []
check = 0
for i in range(80):
    for j in range(len(nota2)):
        if nota[i] == nota2[j]:
            freq_abs[j] += 1
            check = 1
    if check == 0:
        nota2.append(nota[i])
        freq_abs.append(1)
        freq_rel.append(0)
    else:
        check = 0
for i in range(len(nota2)):
    freq_rel[i] = freq_abs[i] * 10 / 8
    print(f'Nota: {nota2[i]:.1f}')
    print(f'Frequência Absoluta: {freq_abs[i]}')
    print(f'Frequência Relativa: {freq_rel[i]:.2f}%')
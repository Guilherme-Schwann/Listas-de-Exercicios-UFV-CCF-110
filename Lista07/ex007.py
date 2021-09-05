v = [int(input()) for x in range(50)]
somp, somi, conp, coni = [0 for x in range(4)]
im = []
p = []
for i in range(50):
    if v[i] % 2 == 0:
        p.append(v[i])
        somp += v[i]
        conp += 1
    else:
        im.append(v[i])
        somi += v[i]
        coni += 1
medias = [somp / conp, somi / coni]
mediap = []
mediai = []
maiorp, menori = p[0], im[0]
for i in p:
    if i > maiorp:
        maiorp = i
    if i > medias[0]:
        mediap.append(i)
for i in im:
    if i < menori:
        menori = i
    if i < medias[1]:
        mediai.append(i)
print(f'Média de números:\n-Pares: {medias[0]}\n-Ímpares: {medias[1]}')
print(f'Maior número par: {maiorp}\nMenor número ímpar: {menori}')
print(f'Números pares maiores que a média PAR: {mediap}')
print(f'Números ímpares menores que a média ÍMPAR: {mediai}')

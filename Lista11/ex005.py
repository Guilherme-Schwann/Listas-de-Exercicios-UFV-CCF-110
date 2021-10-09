nnome, nnota = input('Nome do arquivo com os nomes: '), input('Nome do arquivo com as notas: ')
nomes, notas = open(nnome, "r"), open(nnota, "r")
result = open("Nomes_e_notas.txt", "w")
listanomes, listanotas = nomes.readlines(), notas.readlines()
media = [0 for x in range(len(listanotas))]
for i in range(len(listanomes)-1):
    listanomes[i] = listanomes[i][0:len(listanomes[i])-1]
    listanotas[i] = listanotas[i][0:len(listanotas[i]) - 1]
for i in range(len(listanomes)):
    listanotas[i] = [float(x) for x in listanotas[i].split()]
    soma = 0
    for j in range(len(listanotas[i])):
        soma += listanotas[i][j]
    media[i] = soma / len(listanotas[i])
    result.write(f'{listanomes[i]} - {media[i]:.2f}\n')
nomes.close(), notas.close(), result.close()

nnome, nnota = input('Nome do arquivo com os nomes: '), input('Nome do arquivo com as notas: ')
nomechange = input('Nome do aluno cuja nota será ajustada: ')
oldn, newn = float(input('Nota a ser ajustada: ')), float(input('Nova nota: '))
nomes, notas = open(nnome, "r"), open(nnota, "r")
listanomes, listanotas = nomes.readlines(), notas.readlines()
for i in range(len(listanomes)-1):
    listanomes[i] = listanomes[i][0:len(listanomes[i])-1]
    listanotas[i] = listanotas[i][0:len(listanotas[i]) - 1]
for i in range(len(listanotas)):
    listanotas[i] = [float(x) for x in listanotas[i].split()]
try:
    ind = listanomes.index(nomechange)
    indn = listanotas[ind].index(oldn)
except:
    print('Informações não encontradas!')
    exit()
listanotas[ind].pop(indn)
listanotas[ind].insert(indn, newn)
notas.close(), nomes.close()
notas = open(nnota, "w")
for i in range(len(listanotas)):
    for j in range(len(listanotas[i])):
        if j == len(listanotas[i]) - 1:
            notas.write(f'{listanotas[i][j]}\n')
        else:
            notas.write(f'{listanotas[i][j]} ')
notas.close()
nome1, nome2 = input('Nome do arquivo original: '), input('Nome do arquivo cópia: ')
arq1, arq2 = open(nome1, "r"), open(nome2, "w")
linhas = arq1.readlines()
N = len(linhas)
for i in range(N):
    if linhas[i][0:2] != '//':
        arq2.write(f'{linhas[i]}')
arq1.close()
arq2.close()

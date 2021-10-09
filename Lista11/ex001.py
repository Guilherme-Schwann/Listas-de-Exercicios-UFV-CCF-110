arquivo = open("ex001.txt", "w")
for i in range(200, 50, -1):
    arquivo.write(f'{i}\n')
arquivo.write('50')
arquivo.close()

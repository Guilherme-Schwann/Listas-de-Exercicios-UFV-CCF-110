import random as rd
arq = open("ex003.txt", "w")
N = int(input('Quantidade de nomes e idades: '))
nomes, sobr = [input(f'Nome {i+1}°: ') for i in range(20)], [input(f'Sobrenome {i+1}°: ') for i in range(20)]
for i in range(N):
    idade = rd.randint(1, 100)
    ino, ins = rd.randint(0, 19), rd.randint(0, 19)
    alt = rd.uniform(1.50, 2.00)
    arq.write(f'{nomes[ino]} {sobr[ins]} - {idade} anos - {alt:.2f} m\n')
arq.close()

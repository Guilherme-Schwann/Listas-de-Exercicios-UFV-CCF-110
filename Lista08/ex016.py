m = [[float(input(f'Lucro {j+1}° mês / {i+1}° semana: ')) for i in range(4)] for j in range(12)]
meses = [0 for i in range(12)]
ano = 0
cont = 0
for i in range(12):
    for j in range(4):
        meses[i] += m[i][j]
        cont += 1
        ano += m[i][j]
print(f'Lucros por mês: {meses}')
print(f'Lucros por semana: {m}')
print(f'Lucro anual: R${ano:.2f}')

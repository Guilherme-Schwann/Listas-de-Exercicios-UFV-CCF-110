v = [float(input(f'Tempo do corredor {x+1}: ')) for x in range(10)]
ins = [(x+1) for x in range(10)]
for i in range(10):
    for j in range(9):
        if v[j] > v[j+1]:
            temp, tempinsc = v[j], ins[j]
            v[j], ins[j] = v[j+1], ins[j+1]
            v[j+1], ins[j+1] = temp, tempinsc
for i in range(10):
    print(f'{i+1}° lugar: Tempo: {v[i]} |Número de incrição: {ins[i]}')

m = [[float(input(f'Altura do {i+1}° atleta da {j+1}° delegação: ')) for i in range(10)] for j in range(5)]
maior = [0 for i in range(5)]
for i in range(5):
    maior[i] = m[i][0]
for i in range(5):
    for j in range(10):
        if m[i][j] > maior[i]:
            maior[i] = m[i][j]
for i in range(5):
    print(f'Maior altura da {i+1}° delegação: {maior[i]}')

m = [[0 for i in range(3)] for j in range(50)]
for i in range(50):
    m[i][0] = input('Nome: ')
    m[i][1] = int(input('Estoque ideal: '))
    m[i][2] = int(input('Estoque atual:'))
for i in range(50):
    if m[i][2] < m[i][1]:
        print(f'Nome: {m[i][0]} | Comprar: {m[i][1] - m[i][2]}')

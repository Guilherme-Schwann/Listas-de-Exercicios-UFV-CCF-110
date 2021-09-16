m = [[0 for i in range(4)] for j in range(5)]
ind = 0
for i in range(5):
    m[i][0] = input('Matrícula: ')
    m[i][1] = int(input('Sexo (0 / 1 = Fem / Masc): '))
    m[i][2] = m[i][0][3:6]
    m[i][3] = int(input('CR: '))
cursop = input('Cód. do curso a ser premiado: ')
for i in range(5):
    if m[i][2] == cursop and m[i][1] == 0:
        maior = m[i][3]
for i in range(5):
    if m[i][2] == cursop and m[i][3] > maior and m[i][1] == 0:
        maior = m[i][3]
        ind = i
print(f'Aluna premiada:\nMatrícula: {m[ind][0]}\nCR: {m[ind][3]}\nCód: {m[ind][2]}')

nome = ['x' for x in range(4)]
nota = [0 for x in range(4)]
maior = 0
ind = 0
for i in range(4):
    nome[i] = input('Nome: ')
    nota[i] = float(input('Nota: '))
    if nota[i] > maior:
        maior = nota[i]
        ind = i
print(f'Maior nota:\nNome: {nome[ind]}\nNota: {nota[ind]}')
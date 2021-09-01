vet = [0 for x in range(10)]
for i in range(10):
    vet[i] = int(input('Insira um valor: '))
comp = int(input('Insira um número para comparar com os demais: '))
for j in range(10):
    if vet[j] < comp:
        print(vet[j])
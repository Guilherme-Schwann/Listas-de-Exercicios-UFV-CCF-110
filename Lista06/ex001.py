vet = [0 for x in range(30)]
vet2 = [0 for x in range(30)]
for i in range(30):
    vet[i] = int(input(f'Insira um valor para o vetor {i}: '))
a = int(input('Insira o valor de "a": '))
for j in range(30):
    vet2[j] = vet[j] * a
    if vet2[j] % 2 == 0:
        print(f'{vet[j]} x {a} = {vet2[j]} // Par')
    else:
        print(f'{vet[j]} x {a} = {vet2[j]} // Ímpar')
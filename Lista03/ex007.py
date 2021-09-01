impar = 0
par = 0
for i in range(200):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você inseriu {impar} números ímpares e {par} números pares.')

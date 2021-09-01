maior = int(input())
menor = maior
for i in range(999):
    num = int(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(maior)
print(menor)

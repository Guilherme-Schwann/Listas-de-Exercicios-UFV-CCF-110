soma = 0
cont = 0
while True:
    num = int(input())
    if num <= 0:
        break
    if num % 3 == 0:
        soma += num
        cont += 1
media = soma / cont
print(media)

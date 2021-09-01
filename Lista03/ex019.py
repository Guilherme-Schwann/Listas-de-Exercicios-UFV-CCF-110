soma = 0
for i in range(51):
    divs = 1 + 2 * i
    if i % 2 == 0:
        soma += 1 / pow(divs, 3)
    else:
        soma -= 1 / pow(divs, 3)
pi = (soma * 32) ** (1/3)
print(pi)

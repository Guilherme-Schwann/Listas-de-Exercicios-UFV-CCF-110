a = 0
b = 0
c = 0
d = 0
nul = 0
bran = 0
total = 0
for i in range(10):
    vot = int(input())
    if vot == 1:
        a += 1
    elif vot == 2:
        b += 1
    elif vot == 3:
        c += 1
    elif vot == 4:
        d += 1
    elif vot == 5:
        nul += 1
    elif vot == 6:
        bran += 1
    total += 1
print(f'1 = {a}\n2 = {b}\n3 = {c}\n4 = {d}\nNulo = {nul}\nBranco = {bran}')
print(f'A porcentagem de votos Nulos / Brancos sobre o total é de {100 * (bran + nul) / total}%')

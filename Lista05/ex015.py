print('A: Ótimo\nB: Bom\nC: Regular\nD: Ruim\nE: Péssimo')
a = 0
b = 0
c = 0
d = 0
e = 0
num = 0
sumageD = 0
maiorE = 0
maiorD = 0
maiorA = 0
for i in range(10):
    vt = input('Qual sua nota de A a E? ')
    age = int(input('Qual sua idade? '))
    num += 1
    if vt == 'A' or vt == 'a':
        a += 1
        if age > maiorA:
            maiorA = age
    elif vt == 'B' or vt == 'b':
        b += 1
    elif vt == 'C' or vt == 'c':
        c += 1
    elif vt == 'D' or vt == 'd':
        d += 1
        sumageD += age
        if age > maiorD:
            maiorD = age
    elif vt == 'E' or vt == 'e':
        e += 1
        if age > maiorE:
            maiorE = age
print(a)
porB = 100 * b / num
porC = 100 * c / num
if porB > porC:
    res = porB - porC
else:
    res = porC - porB
print(res)
media = sumageD / d
print(media)
porcE = 100 * e / num
print(porcE, maiorE)
print(maiorA - maiorD)
#Ex.02
raz = int(input('Razão: '))
a1 = int(input('1° termo: '))
n = int(input('N referente ao termo desejado: '))
an = a1 * pow(raz, n - 1)
print(an)
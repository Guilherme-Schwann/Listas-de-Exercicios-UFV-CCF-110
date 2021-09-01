seg = 0
A = 0
B = 2000
while A != B:
    seg += 1
    A += 10
    B -= 15
print(seg)
print(f'Deslocamento de A:{seg*10}\nDeslocamento de B:{seg*15}')

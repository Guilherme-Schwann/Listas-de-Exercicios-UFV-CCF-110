A = 5000000
B = 7000000
ano = 0
while A <= B:
    ano += 1
    A += A * 3 / 100
    B += B * 2 / 100
print(ano)
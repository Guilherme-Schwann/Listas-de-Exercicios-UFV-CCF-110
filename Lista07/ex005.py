v = [int(input()) for x in range(15)]
for i in range(15):
    check = 0
    for j in range(2, v[i]):
        if v[i] % j == 0:
            check += 1
    if check == 0 and v[i] != 1:
        print(f'Primo: {v[i]} / Índice: {i}')
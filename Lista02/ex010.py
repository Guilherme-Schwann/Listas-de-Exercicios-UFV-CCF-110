A = int(input('Insira o 1° valor: '))
B = int(input('Insira o 2° valor: '))
C = int(input('Insira o 3° valor: '))
print('Os 3 valores, em ordem descendente, são:')
if A > B and A > C:
    if B > C:
        print(A, B, C)
    else:
        print(A, C, B)
elif B > A and B > C:
    if A > C:
        print(B, A, C)
    else:
        print(B, C, A)
else:
    if A > B:
        print(C, A, B)
    else:
        print(C, B, A)

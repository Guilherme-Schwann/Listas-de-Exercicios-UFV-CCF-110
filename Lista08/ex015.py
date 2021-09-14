fun = int(input('Quantos funcionários serão pagos? '))
m = [input(f'"Pés", "mãos" e "pés e mãos" feitos pelo {i+1} funcionário (p/m/pm): ').split('/') for i in range(fun)]
sal = [0 for i in range(fun)]
for i in range(fun):
    for j in range(3):
        if j == 0:
            m[i][j] = int(m[i][j]) * 10
        elif j == 1:
            m[i][j] = int(m[i][j]) * 15
        else:
            m[i][j] = int(m[i][j]) * 30
        sal[i] += m[i][j]
for i in range(fun):
    print(f'Salário do {i+1}° funcionário: R${sal[i]:.2f}')

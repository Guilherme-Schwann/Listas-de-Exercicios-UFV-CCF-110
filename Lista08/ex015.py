fun = int(input('Quantos funcionários serão pagos? '))
m = [input(f'"Pés", "mãos" e "pés e mãos" feitos pelo {i+1} funcionário (p/m/pm): ').split('/') for i in range(fun)]
sal = [0 for i in range(fun)]
for i in range(fun):
    m[i][0] = int(m[i][0]) * 10
    m[i][1] = int(m[i][1]) * 15
    m[i][2] = int(m[i][2]) * 30
    sal[i] += m[i][0] + m[i][1] + m[i][2]
for i in range(fun):
    print(f'Salário do {i+1}° funcionário: R${sal[i]:.2f}')

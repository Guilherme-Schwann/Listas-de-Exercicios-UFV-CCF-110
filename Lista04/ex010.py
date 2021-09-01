#Ex.23
notas = input('Insira as notas dos 2 bimestres separadas por espaço (1°bim 2°bim): ')
try:
    nota1 = float(notas.split()[0])
    nota2 = float(notas.split()[1])
    media = (nota1 + nota2) / 2
except:
    print('Notas inválidas.')
    exit()
if media >= 7:
    print('Aprovado.')
elif media < 3:
    print('Reprovado.')
else:
    print('Em exame.')

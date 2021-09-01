peso = float(input('Insira seu peso: '))
alt = float(input('Insira sua altura: '))
imc = peso / alt ** (2)
if imc < 20:
    print('Abaixo do peso.')
elif 20 <= imc < 25:
    print('Peso normal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obeso.')
else:
    print('Obeso mórbido.')

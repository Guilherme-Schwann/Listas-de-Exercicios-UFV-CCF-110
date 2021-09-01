idade = int(input('Insira sua idade: '))
peso = float(input('Insira seu peso:'))
if idade < 0 or peso < 0:
    print('Valores inválidos.')
    exit()
if idade >= 12:
    if peso >= 60:
        dose = 1000
    else:
        dose = 875
else:
    if 5 <= peso < 9:
        dose = 125
    elif 9 <= peso < 16:
        dose = 250
    elif 16 <= peso < 24:
        dose = 275
    elif 24 <= peso < 30:
        dose = 500
    else:
        dose = 750
gotas = (dose / 500) * 20
print(f'Você deve tomar {gotas} gotas por dose.')

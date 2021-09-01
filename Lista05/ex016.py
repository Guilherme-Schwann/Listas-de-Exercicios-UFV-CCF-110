maiorAlt = 0
maiorPeso = 0
quant = 0
somage = 0
while True:
    nome = input('Nome: ')
    if nome == '@':
        break
    sexo = input('Sexo (M ou F): ')
    idade = int(input('Idade: '))
    peso = float(input('Peso: '))
    alt = float(input('Altura: '))
    if sexo == 'M' and alt > maiorAlt:
        maiorAlt = alt
        altnome = nome
    elif sexo == 'F' and peso > maiorPeso:
        maiorPeso = peso
        pesonome = nome
    somage += idade
    quant += 1
print(altnome, maiorAlt)
print(pesonome, maiorPeso)
print(somage / quant)

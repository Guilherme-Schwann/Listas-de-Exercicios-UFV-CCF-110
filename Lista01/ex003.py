tempo = float(input('Insira o tempo gasto na viagem em horas: '))
velmed = float(input('Insira a velocidade média durante a viagem em Km/h: '))
distancia = tempo * velmed
litros = distancia / 12
print(f'A distância percorrida foi de {distancia:.2f} Km/h.')
print(f'Foram consumidos {litros:.2f} litros de combustível durante a viagem.')
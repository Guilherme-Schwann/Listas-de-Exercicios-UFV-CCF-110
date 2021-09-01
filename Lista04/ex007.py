#Ex.11
hora = str(input('Insira o valor hora (HH:MM): ')).split(':')
min = int(hora[1])
min += int(hora[0]) * 60
print(f'Passaram-se {min} minutos desde as 00:00h.')

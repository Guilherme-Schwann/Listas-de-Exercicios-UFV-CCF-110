num = int(input('Insira o número da bola sorteada: '))
din = float(input('Insira o valor do dinheiro restante em caixa: R$'))
if num == 0:
    porc = 5
elif num == 1:
    porc = 25
elif num == 2:
    porc = 10
elif num == 3:
    porc = 7
elif num == 4:
    porc = 8
elif num == 5:
    porc = 5
elif num == 6:
    porc = 15
elif num == 7:
    porc = 12
elif num == 8:
    porc = 3
elif num == 9:
    porc = 10
else:
    print('Número inválido.')
    exit()
premio = din * porc / 100
print(f'Seu prêmio é de R${premio:.2f}')

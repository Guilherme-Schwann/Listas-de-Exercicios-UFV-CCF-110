peso = float(input('Insira seu peso na Terra: '))
print('1)Mercúrio;\n2)Vênus;\n3)Marte;\n4)Júpiter;\n5)Saturno;\n6)Urano;')
plan = int(input('Insira o número correspondente ao planeta desejado: '))
if plan == 1:
    peso = peso * 0.37
elif plan == 2:
    peso = peso * 0.88
elif plan == 3:
    peso = peso * 0.38
elif plan == 4:
    peso = peso * 2.64
elif plan == 5:
    peso = peso * 1.15
elif plan == 6:
    peso = peso * 1.17
else:
    print('Planeta inválido.')
    exit()
print(f'Seu peso nesse planeta é de {peso:.2f} Kg.')

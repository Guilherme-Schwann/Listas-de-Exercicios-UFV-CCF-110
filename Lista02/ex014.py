idade = int(input('Insira sua idade: '))
if idade < 16:
    print(f'Não eleitor.')
elif 18 <= idade < 65:
    print(f'Eleitor obrigatório.')
else:
    print(f'Eleitor facultativo.')

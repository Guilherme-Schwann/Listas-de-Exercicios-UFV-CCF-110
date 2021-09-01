print('Insira sua idade em anos, dias e meses.')
ano = int(input('Anos: '))
mes = int(input('Meses: '))
dia = int(input('Dias: '))
ano = ano * 365
mes = mes * 31
total = ano + mes + dia
print(f'Sua idade é de aproximadamente {total} dias')

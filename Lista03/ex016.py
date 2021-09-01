masc = 0
fem = 0
sim = 0
nao = 0
fs = 0
mn = 0
for i in range(10):
    sx = int(input('Sexo: '))
    ans = int(input('Resposta: '))
    if sx == 1:
        masc += 1
        if ans == 2:
            mn += 1
    elif sx == 2:
        fem += 1
        if ans == 1:
            fs += 1
    if ans == 1:
        sim += 1
    elif ans == 2:
        nao += 1
print(f'{sim} pessoas responderam "Sim" e {nao} pessoas responderam "Não".')
print(f'{100 * fs / fem:.1f}% das pessoas do sexo feminino responderam "Sim".')
print(f'{100 * mn / masc:.1f}% das pessoas do sexo masculino responderam "Não".')

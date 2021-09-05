pre = []
mer = []
quant = []
lucro = 0
for i in range(100):
    pre.append(float(input('Preço da mercadoria: R$')))
    mer.append(int(input('Número da mercadoria: ')))
    quant.append(int(input('Quantidade da mercadoria vendida: ')))
    lucro += pre[i] * quant[i]
print(f'Faturamento mensal: R${lucro:.2f}')

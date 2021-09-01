real = float(input('Preço do dólar: R$'))
qua = int(input('Quantidade de compras: '))
pro = [0 for x in range(qua)]
pre = [0 for x in range(qua)]
for i in range(qua):
    pro[i] = input('Nome do produto: ')
    pre[i] = float(input('Preço do produto: R$'))
for i in range(qua):
    print(f'Produto: {pro[i]}')
    print(f'Peço do produto: ${pre[i]:.2f} / R${pre[i] * real:.2f}')
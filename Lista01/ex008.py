custofab = float(input("Insira o custo de fábrica do carro: "))
dist = custofab * 28 / 100
imp = custofab * 45 / 100
custocons = custofab + dist + imp
print(f'O custo ao consumidor do carro é R${custocons:.2f}')
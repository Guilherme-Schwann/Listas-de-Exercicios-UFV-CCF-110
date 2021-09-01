id = []
val = []
soma, cont = 0, 0
while True:
    vid = int(input('Id: '))
    if vid < 0:
        break
    vval = int(input('Valor a pagar: '))
    id.append(vid)
    val.append(vval)
    cont += 1
    soma += vval
for i in range(cont):
    print(f'Id: {id[i]}\nValor: {val[i]}')
print(f'Total: {soma}')
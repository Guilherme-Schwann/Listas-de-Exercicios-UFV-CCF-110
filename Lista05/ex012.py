gr = int(input())
cont = 1
fat = 1
rad = gr / 180
res = 0
for i in range(15):
    fat = 1
    for j in range(cont):
        j += 1
        fat *= j
    mod = rad ** cont / fat
    if i % 2 == 0:
        res += mod
    else:
        res -= mod
    cont += 2
print(res)

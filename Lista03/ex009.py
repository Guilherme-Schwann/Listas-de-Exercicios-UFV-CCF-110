media = float(0)
num = 0
quant = 0
while num >= 0:
    num = int(input())
    if num >=0:
        media += num
        quant += 1
print(media / quant)
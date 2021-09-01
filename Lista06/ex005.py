v = [0 for x in range(15)]
sum = 0
for i in range(15):
    v[i] = int(input())
    sum += v[i]
print(f'Média: {sum / 15}')
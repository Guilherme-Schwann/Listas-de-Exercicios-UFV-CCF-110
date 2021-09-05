v = [int(input()) for x in range(100)]
sum = 0
for i in range(int(100/2)):
    sum += (v[i] - v[99-i]) ** 3
print(sum)

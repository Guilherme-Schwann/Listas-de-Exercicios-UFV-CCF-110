v1 = [int(input()) for x in range(10)]
v2 = []
for i in range(10):
    v2.append(v1[9 - i])
print(v2)

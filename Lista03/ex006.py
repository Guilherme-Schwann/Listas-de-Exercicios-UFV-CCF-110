x = int(input())
z = int(input())
if x < z:
    for i in range(x, z + 1):
        print(i)
elif x > z:
    for i in range(x, z - 1, -1):
        print(i)
else:
    print(z)

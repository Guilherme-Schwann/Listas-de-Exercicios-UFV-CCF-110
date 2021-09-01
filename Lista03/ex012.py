a = int(1)
b = int(0)
for i in range(10):
    print(a)
    b += a
    a += b
    print(b)

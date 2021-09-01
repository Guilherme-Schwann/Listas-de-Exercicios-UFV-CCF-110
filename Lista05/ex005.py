NUM = int(input())
for i in range(NUM):
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        print(i + 1)
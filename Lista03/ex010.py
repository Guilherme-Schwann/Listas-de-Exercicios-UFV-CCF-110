N = int(input())
if N == 0:
    fat = 1
else:
    i = 1
    fat = 1
    while i <= N:
        fat *= i
        i += 1
print(fat)

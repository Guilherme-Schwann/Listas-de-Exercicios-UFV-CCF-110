N = int(input())
if N == 0:
    fat = 1
else:
    fat = 1
    for i in range(1, N + 1):
        fat *= i
print(fat)

M = [[int(input()) for i in range(2)] for j in range(2)]
pp, ps = 1, 1
for i in range(2):
    pp *= M[i][i]
    ps *= M[i][1-i]
det = pp - ps
print(det)

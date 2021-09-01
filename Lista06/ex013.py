v = [int(input()) for x in range(5)]
for i in range(5):
    print(v[i], end=' ')
cres = []
print()
for i in range(5):
    a = v[i]
    if i == 0 or v[i] >= cres[-1]:
        cres.append(v[i])
    else:
        for b in range(len(cres)):
            if a < cres[b]:
                cres.insert(b, a)
                break
for i in range(5):
    print(cres[i], end=' ')

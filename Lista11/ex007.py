ips = open("ex007ips.txt", "r")
val, inv = open("ex007val.txt", "w"), open("ex007inv.txt", "w")
linhas = ips.readlines()
for i in range(len(linhas)):
    temp = linhas[i].split('.')
    check = 0
    for j in range(len(temp)):
        temp[j] = int(temp[j])
        if j == 0 and 1 <= temp[j] <= 255:
            check += 1
        elif j != 0 and 0 <= temp[j] <= 255:
            check += 1
    if check == len(temp):
        val.write(linhas[i])
    else:
        inv.write(linhas[i])
ips.close(), val.close(), inv.close()

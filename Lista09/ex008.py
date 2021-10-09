m = [[int(input()) for i in range(10)] for j in range(10)]
temp = [0 for i in range(10)]
for i in range(10):
    print(m[i])
for i in range(10):
    #Troca a segunda e a oitava linha:
    temp[i] = m[1][i]
    m[1][i] = m[7][i]
    m[7][i] = temp[i]
for i in range(10):
    #Troca a quarta e a décima linha:
    temp[i] = m[i][3]
    m[i][3] = m[i][9]
    m[i][9] = temp[i]
for i in range(10):
    #Troca a diagonal principal pela secundária e vice-versa:
    temp[i] = m[i][i]
    m[i][i] = m[i][9-i]
    m[i][9-i] = temp[i]
for i in range(10):
    print(m[i])

n = int(input())
prodimp = 1
sompar = 0
if n == 0:
    prodimp = 0
while n > 0:
    if n % 2 == 1:
        prodimp *= n
    else:
        sompar += n
    n = int(input())
print(f'O produto dos números ímpares é {prodimp}')
print(f'A soma dos números pares é {sompar}')
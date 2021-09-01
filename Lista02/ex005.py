num1 = int(input('Insira o dividendo: '))
num2 = int(input('Insira o divisor: '))
if num2 == 0:
    print('Divisão não permitida')
else:
    quo = int(num1 / num2)
    resto = num1 % num2
    print(f'O quociente de {num1} / {num2} é {quo}, e o resto dessa divisão é {resto}')

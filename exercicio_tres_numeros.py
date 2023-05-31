numero = int(input('digite o primeiro numero : '))
numero1 = int(input('digite o segundo numero : '))
numero2 = int(input('digite o terceiro numero : '))

if numero > numero1  and numero > numero2:
    print(f'o maior numero é {numero}')
elif numero1 > numero and numero1 > numero2:
    print(f'o maior numero é {numero1}')
else:
    print(f'o maior numero é {numero2}')
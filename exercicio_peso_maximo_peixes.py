peso = int(input('digite o peso: '))


if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

elif peso < 50:
    excesso = 'zero'
    multa = 'zero'

print(f'o excesso de peso é de {excesso} kg, e sua multa foi de r${multa}')

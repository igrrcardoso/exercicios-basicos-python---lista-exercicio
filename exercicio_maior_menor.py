"""
escreva um programa que leia três numeros e mostre o maior e o menor deles
"""

numero = int(input('digite o primeiro numero : '))
numero1 = int(input('digite o segundo numero : '))
numero2 = int(input('digite o terceiro numero : '))


#bloco maior numero
if numero > numero1 and numero > numero2:
    print(f'o maior numero é : {numero}')
if numero1 > numero and numero1 > numero2:
    print(f'o maior numero é : {numero1}')
if numero2 > numero and numero2 > numero1:
    print(f'o maior numero é : {numero2}')

#bloco menor numero
if numero < numero1 and numero < numero2:
    print(f'o menor numero é : {numero} ')
if numero1 < numero and numero1 < numero2:
    print(f'o menor numero é : {numero1} ')
if numero2 < numero and numero2 < numero1:
    print(f'o menor numero é : {numero2} ')






# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('digite um numero : '))

#bloco variaveis
positivo = numero >= 0
negativo = numero < 0

if positivo:
    print(f'o número é {numero} e é positivo')
elif negativo:
    print(f'o número é {numero} e é negativo')
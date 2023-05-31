"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

metros2 = float(input('qual o tamanho da área a ser pintada ? '))


litros = metros2 / 3
latas = litros / 18
preco = latas * 80
if litros % 18 != 0:
    latas += 1

print(f'''
a quantidade de latas de tinta que serão necessarias são : {latas:.2f}
o preço total é {preco:,.2f}
''')

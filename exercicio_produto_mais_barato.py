"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

produto_a = input('qual o preço do produto ? ')
produto_b = input('qual o preço do outro produto ? ')
produto_c = input('qual o preço do ultimo produto ? ')

menor_preco = produto_a

if menor_preco < produto_b and menor_preco < produto_c:
    menor_preco
elif produto_b < menor_preco and produto_b < produto_c:
    menor_preco = produto_b
else:
    menor_preco = produto_c


print(f'o produto escolhido pelo menor preço é : {menor_preco}')

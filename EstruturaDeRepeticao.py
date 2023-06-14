"""
Exercicio - 1
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
"""

# while True:
#     nota = input('Dê uma nota de 0 à 10: ')

#     try:
#         nota_int = int(nota)
#         if nota_int > 10:
#             print('''
# ERRO
# Valor Inválido.
# ''')
#             continue
#     except ValueError:
#         print('Você digitou letras no lugar de números.')
#         continue

#     if nota_int in range(0, 11):
#         print('Valor Válido.')
#         break

"""
Exercicio - 2
Faça um programa que leia um nome de usuário e a sua senha e não aceite
a senha igual ao nome do usuário, mostrando uma mensagem de erro
e voltando a pedir as informações.
"""

# while True:

#     nome = input('Digite seu nome: ')
#     senha = input('Digite sua senha: ')

#     if senha == nome:
#         print('ERRO\nSua senha não pode ser igual ao seu nome.')
#         continue
#     else:
#         print('Informações Válidas.')
#         break

"""
Exercicio - 3
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""


# while True:
#     nome = input('digite seu nome: ')
#     idade = input('digite sua idade: ')
#     salário = input('digite seu salário: ')
#     sexo = input('Sexo [f] ou [m]: ').lower()
#     estado_civil = input('Qual seu estado civil: [s], [c], [v], [d]: ')

#     try:
#         salario_float = float(salário)
#         int_idade = int(idade)

#         if len(nome) < 3:
#             raise ValueError('ERRO\nNome muito curto.')
#         elif int_idade > 150:
#             raise ValueError('ERRO\nIdade maior que 150 anos.')
#         elif salario_float <= 0:
#             raise ValueError('ERRO\n Salário inferior a 0.')
#         elif sexo not in ['f', 'm']:
#             raise ValueError('ERRO\n Sexo Inválido.')
#         elif estado_civil not in ['s', 'c', 'v', 'd']:
#             raise ValueError('ERRO\n Estado Civil Inválido.')
#     except ValueError:
#         print('Valor Inválido, confira as informações digitadas.')
#         break


"""
Exercicio - 4
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa
de crescimento de 1.5%. Faça um programa que calcule e escreva
o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""
# populacao_A = 80000
# populacao_B = 200000
# ano = 0
# taxa_A = 0.03
# taxa_B = 0.015

# while populacao_A < populacao_B:
#     populacao_A += populacao_A * taxa_A
#     populacao_B += populacao_B * taxa_B
#     ano += 1

# print(f'''
# em {ano} anos a população A teria: {populacao_A:,.3f}\n
# E a população B teria: {populacao_B:,.3f}
#       ''')

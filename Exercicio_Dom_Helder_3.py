"""
Comando de repetição for
"""

"""
Exercício - 1
Faça um programa que calcule os valores da função
f(x) = x² - 1, para 10 valores de x informados pelo usuário.
A cada valor informado o programa deverá imprimir este valor e o da função
da seguinte forma:

x=1 f(x) = 0
x=2 f(x) = 3
x=3 f(x) = 8
...
x=10 f(x) = 99
"""

# for f in range(0, 10):
#     valor_x = int(input('Entre com o valor de x: '))
#     funcao = (valor_x ** 2) - 1
#     print(f'x={valor_x} f(x) = {funcao}')

"""
Exercício - 2
Faça um programa para calcular e imprimir a área de 10 círculos,
cujos raios serão informados pelo usuário. Use o valor de ~ igual a 3.1416.

Área = piR²

Para testar:
Raio = 60 -> Área = 11309.76
Raio = 99 -> Área = 30790.8216
Raio = 45 -> Área = 6361.74
"""
# PI = 3.1416

# for calculo in range(0, 10):
#     raio = input('Entre com o raio do círculo: ')
#     raio_float = float(raio)
#     area = PI * (raio_float ** 2)
#     print(area)

"""
Exercício - 3
Faça um programa para ler a nota final e
o total de faltas de todos os 50 alunos de uma disciplina.
A cada aluno lido o programa deverá verificar e informar
se o aluno foi APROVADO ou REPROVADO.
Se o aluno tiver obtido nota igual ou superior a 65
e não tiver faltado a mais de 16 aulas ele foi aprovado,
senão ele foi reprovado.

Para testar:
Nota = 75 e Falta = 12  ALUNO APROVADO
Nota = 99 e Falta = 20  ALUNO REPROVADO
Nota = 45 e Falta = 11  ALUNO REPROVADO
Nota = -1

Observação: Interrompa as repetições se o usuário digitar -1 na nota final.
"""

# for resultado in range(0, 50):
#     nota_final = input('Digite sua nota final: ')
#     faltas = input('Digite quantas faltas você teve: ')
#     float_nota = float(nota_final)
#     int_faltas = int(faltas)

#     if float_nota >= 65 and int_faltas <= 16:
#         resultado = 'Aprovado'
#     elif float_nota == -1:
#         print('Não pode digitar -1 :(')
#         break
#     else:
#         resultado = 'Reprovado'
#     print(f'ALUNO {resultado.upper()}')

"""
Exercício - 4
Faça um programa que leia o nome e sexo
(“M” para masculino e “F” para feminino) de um grupo de 100 pessoas
e ao final imprima a quantidade de mulheres.
"""

# qtd_homens = 0
# qtd_mulheres = 0

# for genero in range(0, 100):
#     nome = input('Diga seu nome: ')
#     genero = input('Qual seu sexo [M] ou [F]: ').capitalize()
#     if genero == 'F':
#         qtd_mulheres += 1
#     elif genero == 'M':
#         qtd_homens += 1
#     else:
#         print('Valor Inválido, use [F] para feminino ou [M] para masculino')

# print(f'''
# a quantidade de mulheres é: {qtd_mulheres}
# e a de homens é {qtd_homens}
#     ''')

"""
Faça um programa que calcule e imprima a quantidade de postos de gasolina
cujos preços estão abaixo de R$3,00 e a quantidade de postos cujos preços
ultrapassam os R$4,00. Para isto o programa deverá ler
o nome e o preço da gasolina de 68 postos de gasolina pesquisados.
"""

# erro = ''
# qtd_postos_menor_preco_gasolina = 0
# qtd_postos_maior_preco_gasolina = 0

# for i in range(0, 68):
#     nome_posto = input('Entre com o nome do posto: ')
#     preco_gasolina = input('Entre com o preço da gasolina: ')
#     preco_gasolina_float = float(preco_gasolina)
#     if preco_gasolina_float < 3:
#         qtd_postos_menor_preco_gasolina += 1
#     elif preco_gasolina_float > 4:
#         qtd_postos_maior_preco_gasolina += 1
#     else:
#         print('Valor deve ser menor que 3 ou maior que 4')

#     if nome_posto.isdigit():
#         erro = 1
#     elif not preco_gasolina.isdigit():
#         erro = 2
#     else:
#         erro = 3

#     if erro == 1:
#         print('O nome do posto não pode ser um dígito.')
#         continue
#     elif erro == 2:
#         print('O preço da gasolina precisa ser um dígito')
#     elif erro == 3:
#         print('Valor Inválido.')

# menor_preco = qtd_postos_menor_preco_gasolina
# maior_preco = qtd_postos_maior_preco_gasolina

# print(f'''
# Quantidade de postos com a gasolina abaixo de 3R$: {menor_preco}
# Quantidade de postos com a gasolina acima de 4R$: {maior_preco}
#     ''')


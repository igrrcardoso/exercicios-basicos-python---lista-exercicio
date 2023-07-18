import os
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

"""
Faça um programa que calcule, entre 5 números informados pelo usuário,
a quantidade de números NEGATIVOS e a quantidade de números POSITIVOS
(incluindo o zero).
"""
# numeros_negativos = 0
# numeros_positivos = 0

# for i in range(0, 5):
#     numeros = int(input('Informe um número: '))
#     if numeros < 0:
#         numeros_negativos += 1
#     elif numeros >= 0:
#         numeros_positivos += 1
#     else:
#         print('Valor Inválido')

# print(f'Quantidade de números negativos = {numeros_negativos}\n'
#       f'Quantidade de números positivos = {numeros_positivos}')

'''
Exercício - 5
Faça um programa para ler a nota final e o total de faltas
de todos os 50 alunos de uma disciplina.
A cada aluno lido o programa deverá verificar e informar
se o aluno foi APROVADO ou REPROVADO.
Se o aluno tiver obtido nota igual ou superior a 65
e não tiver faltado a mais de 16 aulas ele foi aprovado,
senão ele foi reprovado.
Ao final do programa deverão ser informados quantos alunos foram aprovados
e quantos foram reprovados.
'''

# quantidade_alunos_reprovados = 0
# quantidade_alunos_aprovados = 0
# reprovado = ''
# aprovado = ''

# for i in range(0, 3):
#     nota_final = float(input('Entre com sua nota final: '))
#     faltas = int(input('Entre com a quantidade de faltas: '))
#     if nota_final >= 65 and faltas <= 16:
#         aprovado = 'Aluno Aprovado'
#         quantidade_alunos_aprovados += 1
#         print(aprovado)
#     elif nota_final < 65:
#         reprovado = 'Aluno Reprovado'
#         quantidade_alunos_reprovados += 1
#         print(reprovado)
#     elif faltas > 16:
#         reprovado = 'Aluno Reprovado'
#         quantidade_alunos_reprovados += 1
#         print(reprovado)
#     else:
#         print('Valor Inválido.')

# print(f'aprovados = {quantidade_alunos_aprovados}\n'
#       f'reprovados = {quantidade_alunos_reprovados}')

"""
Exercício - 6
Fazer um programa para ler o nome e a idade de todos os 50 alunos
de uma turma e calcular e imprimir:

a) Quantos alunos tem até 18 anos
b) Quantos alunos tem acima de 18 anos
"""

# quantidade_acima_18 = 0
# quantidade_ate_18 = 0

# for alunos in range(0, 50):
#     nome = input('Informe seu nome: ')
#     idade = int(input('Entre com sua idade: '))

#     if idade <= 18:
#         quantidade_ate_18 += 1
#     elif idade > 18:
#         quantidade_acima_18 += 1
#     else:
#         print('valor inválido.')

# print(f'Até 18: {quantidade_ate_18}\nAcima de 18: {quantidade_acima_18}')

"""
Faça um programa para apurar as eleições para prefeito de uma cidade.
Para o cargo se candidataram 3 pessoas: Fulano, Ciclano e Beltrano.
O programa deverá ler todos os votos, calcular e imprimir a
quantidade de votos obtido por cada candidato e o nome do candidato vencedor.
A cidade tem 100 eleitores e todos votaram

Observações:
1) O voto será computado pelo número do candidato
e não pelo seu nome de acordo com a codificação abaixo:
1 - Fulano, 2 - Ciclano e 3 - Beltrano
2) Não haverá votos em branco ou nulos.
3) Não haverá empate entre candidatos.
"""

# candidatos = ['Fulano', 'Ciclano', 'Beltrano']
# contador_fulano = 0
# contador_ciclano = 0
# contador_beltrano = 0


# for eleitores in range(0, 100):
#     lista_candidatos = input('aperte [L] para ver a lista de candidatos: ')\
#         .capitalize()

#     for indice, nome in enumerate(candidatos, start=1):
#         if lista_candidatos == 'L':
#             print(indice, nome)

#     votos = int(input('Digite o número do candidato em que deseja votar: '))
#     if votos == 1:
#         contador_fulano += 1
#         continue
#     elif votos == 2:
#         contador_ciclano += 1
#         continue
#     elif votos == 3:
#         contador_beltrano += 1
#         continue
#     else:
#         print('Não será permitido votos em branco')

#     if contador_fulano == contador_ciclano:
#         print('Não pode haver empates, então será refeita a votação.')
#         break
#     elif contador_fulano == contador_beltrano:
#         print('Não pode haver empates, então será refeita a votação.')
#         break
#     elif contador_ciclano == contador_beltrano:
#         print('Não pode haver empates, então será refeita a votação.')
#         break

# os.system('cls')


# if contador_ciclano > contador_beltrano and contador_ciclano >\
#    contador_fulano:
#     print(
#      f'O vencedor foi Ciclano com {contador_ciclano} votos\n'
#      f'Fulano teve {contador_fulano} votos\n'
#      f'Beltrano teve {contador_beltrano} votos', end=''
#     )
# elif contador_beltrano > contador_ciclano and contador_beltrano >\
#      contador_fulano:
#     print(
#      f'O vencedor foi Beltrano com {contador_beltrano} votos\n'
#      f'Fulano teve {contador_fulano} votos\n'
#      f'Ciclano teve {contador_ciclano} votos', end=''
#     )
# elif contador_fulano > contador_beltrano and contador_fulano >\
#      contador_ciclano:
#     print(
#      f'O vencedor foi Fulano com {contador_fulano} votos\n'
#      f'Ciclano teve {contador_ciclano} votos\n'
#      f'Beltrano teve {contador_beltrano} votos', end=''
#     )
# else:
#     print('Valor Inválido')

"""
Refaça, complementando o programa anterior, prevendo que poderá haver
empate triplo ou duplo entre os candidatos, e, se houver empates,
continue o programa fazendo um segundo turno somente com os candidatos
que empataram.

Também faça o programa contar os votos nulos (diferentes de 1, 2 ou 3) e,
se a quantidade de votos nulos for maior do que a quantidade de votos válidos
(soma dos votos dados aos candidatos 1, 2 e 3),
o programa deverá informar que a eleição, inclusive a de segundo turno,
está anulada.
"""

# candidatos = ['Fulano', 'Ciclano', 'Beltrano']
# contador_fulano = 0
# contador_ciclano = 0
# contador_beltrano = 0
# contador_votos_em_branco = 0
# empate = False

# for eleitores in range(0, 5):
#     lista_candidatos = input('aperte [L] para ver a lista de candidatos: ')\
#         .capitalize()

#     for indice, nome in enumerate(candidatos, start=1):
#         if lista_candidatos == 'L':
#             print(indice, nome)

#     votos = int(input('Digite o número do candidato em que deseja votar: '))
#     if votos == 1:
#         contador_fulano += 1
#         continue
#     elif votos == 2:
#         contador_ciclano += 1
#         continue
#     elif votos == 3:
#         contador_beltrano += 1
#         continue
#     else:
#         contador_votos_em_branco += 1

#     if contador_fulano == contador_ciclano or contador_fulano ==\
#        contador_beltrano:
#         empate = True
#     else:
#         empate = False

#     if empate is True:
#         print('Iniciando o segundo turno\nMotivo:EMPATE')
#         candidatos_empatados = []
#         if contador_fulano == max(contador_ciclano, contador_beltrano,
#                                   contador_fulano):
#             candidatos_empatados.append('Fulano')
#         elif contador_ciclano == max(contador_fulano, contador_ciclano,
#                                      contador_beltrano):
#             candidatos_empatados.append('Ciclano')
#         elif contador_beltrano == max(contador_fulano, contador_ciclano,
#                                       contador_beltrano):
#             candidatos_empatados.append('Beltrano')

#             for indice, nome in enumerate(candidatos_empatados, start=1):
#                 print(indice, nome)


# os.system('cls')

# if empate != 0:
#     if contador_ciclano > contador_beltrano and contador_ciclano > contador_fulano:
#         print(
#             f'O vencedor foi Ciclano com {contador_ciclano} votos\n'
#             f'Fulano teve {contador_fulano} votos\n'
#             f'Beltrano teve {contador_beltrano} votos', end=''
#         )
# elif contador_beltrano > contador_ciclano and contador_beltrano >\
#      contador_fulano:
#     print(
#      f'O vencedor foi Beltrano com {contador_beltrano} votos\n'
#      f'Fulano teve {contador_fulano} votos\n'
#      f'Ciclano teve {contador_ciclano} votos', end=''
#     )
# elif contador_fulano > contador_beltrano and contador_fulano >\
#      contador_ciclano:
#     print(
#      f'O vencedor foi Fulano com {contador_fulano} votos\n'
#      f'Ciclano teve {contador_ciclano} votos\n'
#      f'Beltrano teve {contador_beltrano} votos', end=''
#     )
# else:
#     print('Valor Inválido')

# candidatos = ['Fulano', 'Ciclano', 'Beltrano']

# contador_fulano = 0
# contador_ciclano = 0
# contador_beltrano = 0
# contador_votos_nulos = 0

# for eleitores in range(0, 5):
#     lista_candidatos = input('Aperte [L] para ver a lista de candidatos: ').capitalize()

#     if lista_candidatos == 'L':
#         for indice, nome in enumerate(candidatos, start=1):
#             print(indice, nome)

#     votos = int(input('Digite o número do candidato em que deseja votar: '))

#     if votos == 1:
#         contador_fulano += 1
#     elif votos == 2:
#         contador_ciclano += 1
#     elif votos == 3:
#         contador_beltrano += 1
#     else:
#         contador_votos_nulos += 1

# total_votos_validos = contador_fulano + contador_ciclano + contador_beltrano

# if contador_votos_nulos > total_votos_validos:
#     print('A eleição está anulada.')
# else:
#     empate = False

#     if contador_fulano == contador_ciclano or contador_fulano == contador_beltrano or contador_ciclano == contador_beltrano:
#         empate = True

#     if empate:
#         print('Houve empate. Segundo turno entre os candidatos empatados:')
#         candidatos_empatados = []
#         if contador_fulano == max(contador_fulano, contador_ciclano, contador_beltrano):
#             candidatos_empatados.append('Fulano')
#         if contador_ciclano == max(contador_fulano, contador_ciclano, contador_beltrano):
#             candidatos_empatados.append('Ciclano')
#         if contador_beltrano == max(contador_fulano, contador_ciclano, contador_beltrano):
#             candidatos_empatados.append('Beltrano')

#         for indice, nome in enumerate(candidatos_empatados, start=1):
#             print(indice, nome)

#         votos_segundo_turno = int(input('Digite o número do candidato em que deseja votar no segundo turno: '))

#         if votos_segundo_turno == 1:
#             contador_fulano += 1
#         elif votos_segundo_turno == 2:
#             contador_ciclano += 1
#         elif votos_segundo_turno == 3:
#             contador_beltrano += 1

#     if contador_fulano > contador_ciclano and contador_fulano > contador_beltrano:
#         print(f'O vencedor foi Fulano com {contador_fulano} votos')
#     elif contador_ciclano > contador_fulano and contador_ciclano > contador_beltrano:
#         print(f'O vencedor foi Ciclano com {contador_ciclano} votos')
#     elif contador_beltrano > contador_fulano and contador_beltrano > contador_ciclano:
#         print(f'O vencedor foi Beltrano com {contador_beltrano} votos')
#     else:
#         print('Houve empate novamente ou nenhum voto foi dado aos candidatos.')

# calculadora teste rápido

numero1 = input('Digite o primeiro número: ')
operador = input('Digite o operador que deseja usar "+, -, /, %: ')
numero2 = input('Digite o segundo número: ')

soma = 0
subtracao = 0
divisao = 0
porcentagem = 0

try:
    numero1_int = int(numero1)
    numero2_int = int(numero2)

except ValueError as ve:
    print('Use apenas dígitos', ve)

if operador == '+':
    soma = numero1_int + numero2_int
    print(soma)
elif operador == '-':
    subtracao = numero1_int - numero2_int
    print(subtracao)
elif operador == '/':
    divisao = numero1_int // numero2_int
    print(divisao)
elif operador == '%':
    porcentagem = numero1_int % numero2_int
    print(porcentagem)
else:
    print('Você usou um operador inválido!')

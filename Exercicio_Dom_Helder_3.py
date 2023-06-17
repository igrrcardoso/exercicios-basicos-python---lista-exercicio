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



"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
# bibliotecas importadas
import os

# input para entrar no programa
entrar = input('aperte "enter" para entrar no programa : ')

if entrar == "":
    ...
else:
    print('Saindo do programa...')
    exit()

# bloco para calcular horas mensais trabalhadas
calcular_horas_mensais = float(input('horas trabalhadas por dia : '))
sabado = input('Trabalha sábado ? "(S) ou (N)" : ')
os.system('cls')

if sabado == 'S':
    calcular_horas_mensais *= 6 * 4
    print(f'as suas horas trabalhadas no mês são : {calcular_horas_mensais}')
elif sabado == 'N':
    calcular_horas_mensais *= 5 * 4
    print(f'as suas horas trabalhadas no mês são : {calcular_horas_mensais}')
else:
    print('você não inseriu nada no campo, favor digitar S ou N.')

# bloco para calcular o salario e os descontos
dinheiro_por_hora = float(input('quanto você ganha por hora? '))
salario_mensal = dinheiro_por_hora * calcular_horas_mensais
ir = (salario_mensal * 11) / 100
inss = (salario_mensal * 8) / 100
sindicato = (salario_mensal * 5) / 100
salario_liquido = salario_mensal - ir - inss - sindicato
os.system('cls')

print(f'''
    + Salário Bruto : R${salario_mensal:,.2f}
    - IR (11%) : R${ir:,.2f}
    - INSS (8%) : R${inss:,.2f}
    - Sindicato (5%) : R${sindicato:,.2f}
    = Salário liquido : R$ {salario_liquido:,.2f}
''')

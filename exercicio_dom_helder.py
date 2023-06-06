# Faça um programa para calcular e imprimir o valor a ser descontado de INSS no salário
# de um empregado utilizando a tabela abaixo. O usuário fornecerá o salário.
#Até      R$300,00 Alíquota 8%
#Acima de R$300,00 Alíquota 10%


# salario = int(input('digite seu salário: '))

# if salario <= 300:
#     desconto = (salario * 0.08)
#     print('funcionario caiu na alíquota de 8%')
# else:
#     desconto = (salario * 0.10)
#     print('funcionario caiu na alíquota de 10%')


# print(desconto)

#exemplo 2

# Faça um programa para calcular e imprimir o valor a ser descontado de INSS no salário
# de um empregado utilizando a tabela abaixo. O usuário fornecerá o salário.

"""
Faixa salarial                   Alíquota
Até R$300,00                          8%
Acima de R$300,00 até R$1000,00       9%
Acima de R$1000,00                    10%"""

# salario = float(input('digite seu salário: '))

# if salario <= 300:
#     desconto = (salario * 0.08)
# elif salario > 300 and salario <= 1000:
#     desconto = (salario * 0.09)
# else:
#     desconto = (salario * 0.10)

# print(desconto)


"""
Exercicio - 3
A Secretaria do Meio Ambiente mediu a quantidade de poluentes atmosféricos emitidos
por uma empresa. Dependendo do valor obtido, a empresa foi multada conforme a tabela abaixo.
Faça um programa que leia a quantidade de poluentes emitidos por uma empresa e calcule e imprima
a multa aplicada, se for o caso.

Quantidade de poluente emitido      Valor da Multa
Até 1500                            Isento
Acima de 1500 até 3500              R$3.000,00
Acima de 3500                       R$5.000,00 x quantidade de poluente
"""

# qtd_poluente = float(input('qual a quantidade de poluente? '))

# if qtd_poluente <= 1500:
#     multa = 0
# elif qtd_poluente > 1500 and qtd_poluente <= 3500:
#     multa = 3000.00
# else:
#     multa = (5000.00 * qtd_poluente)

# print(f'{multa:,.2f}')

"""
Exercicio-4
Faça um programa que calcule o salário mensal a receber de um vendedor comissionado.
O salário é constituído de um valor fixo de R$240,00 mais o valor referente a comissão,
calculada de acordo com a tabela abaixo, que varia com as vendas mensais realizadas pelo vendedor.
O programa deverá solicitar ao usuário o valor mensal das vendas do vendedor e calcular e imprimir
o seu salário no mês.

                    SALÁRIO = VALOR FIXO + COMISSÃO
                    
TOTAL MENSAL VENDIDO                        CÁLCULO DA COMISSÃO
Até R$1,000.00                                     Zero
Acima de R$1,000.00 até R$10,000.00       10% sobre o valor vendido
Acima de R$10,000.00                         R$ 1,000.00 fixos
"""

# valor_vendas = float(input('qual o valor de vendas deste mês? '))

# if valor_vendas <= 1000:
#     comissao = 240
# elif valor_vendas > 1000 and valor_vendas <= 10000:
#     comissao = (valor_vendas * 0.10) + 240
# else:
#     comissao = (1000 + 240)

# print(comissao)

"""
Exercicio - 5

Faça um programa para ler o nome, a altura (em metros) e o peso (em kg) de uma pessoa
e informar a ela a sua situação corporal de acordo com o seu IMC (Índice de Massa Corporal)
que será calculado pelo programa
   
            IMC = Peso / Altura2

IMC menor que 18  pessoa está desnutrida
IMC menor que 20  pessoa está abaixo do peso
IMC entre 20 e 25  pessoa está no peso ideal
IMC maior que 25  pessoa está acima do peso
IMC maior que 27  pessoa está obesa
"""

# nome = input('seu nome: ')
# altura = float(input('sua altura: '))
# peso = float(input('quanto você pesa em kg: '))

# imc = peso/(altura*altura)

# if imc < 18:
#     print(f'{nome} está desnutrido')
# elif imc < 20:
#     print(f'{nome} está abaixo do peso')
# elif imc <= 25:
#     print(f'{nome} está no peso ideal')
# elif imc <= 27:
#     print(f'{nome} está acima do peso')
# else:
#     print(f'{nome} está obeso')

"""
Exercicio- 6
Faça um programa que solicite ao usuário um número inteiro e calcule e imprima se ele é divisível ao mesmo tempo por 5 e 7.

Observação: Para testarmos se um número é divisível por outro utilizamos o operador % (RESTO DE UMA DIVISÃO INTEIRA). 

Exemplo  Se X % 2 = 0 
estamos constatando que X é divisível por 2.

"""

# numero_int = int(input('digite o número: '))

# if numero_int % 5 == 0 and numero_int % 7 == 0:
#     print(f'{numero_int} é divisivel simultaneamente por 5 e 7.')
# else:
#     print(f'{numero_int} não é divisivel simultaneamente por 5 e 7')

"""
Exercicio-7
Pela fórmula de Báskara abaixo calculamos as raízes reais de uma equação do segundo grau.
Faça um programa para solicitar ao usuário os valores de A, B e C
e calcular e imprimir as raízes da função f(x).
"""

# a = float(input('qual o valor de "a" ? '))
# b = float(input('qual o valor de "b" ? '))
# c = float(input('qual o valor de "c" ? '))


"""
A legislação brasileira prevê a distribuição dos lucros
de uma empresa semestralmente. Cada empresa faz esta distribuição
proporcional ao salário de cada empregado e com cálculos
específicos. Faça um programa que solicite ao usuário o salário
de um empregado e calcule e imprima o valor de sua participação
nos lucros (PL Líquido) de acordo com a tabela e fórmulas abaixo:

Salário                    Valor Fixo            % Sobre o salário
Até R$300                     R$500                      70%
Acima de R$300 até R$1000     R$200                      50%
Acima de R$1000               Zero                       30%


PL Bruto = Valor Fixo + Percentual sobre o Salário
Imposto de Renda = 25% sobre PL Bruto
PL Líquido = PL Bruto - Imposto de Renda
"""

# while True:

#     nome = input('digite o nome do empregado: ')
#     salario = input('digite o salário deste empregado: ')

#     valor_invalido = None
#     salario_float = 0
#     pl_bruto = 0
#     pl_liquido = 0
#     imposto_renda = 0

#     try:
#         salario_float = float(salario)
#         valor_invalido = True
#     except:
#         valor_invalido = None
#         print('Você digitou um valor inválido no campo "salário".')
#         continue

#     if nome.isnumeric():
#         print('Valor Inválido. Você digitou números no lugar de nomes.')
#         continue
# ###

#     if salario_float <= 300:
#         pl_bruto = (salario_float * 0.70) + 500
#         imposto_renda = pl_bruto * 0.25
#         pl_liquido = pl_bruto - imposto_renda

#     elif salario_float > 300 and salario_float <= 1000:
#         pl_bruto = (salario_float * 0.50) + 200
#         imposto_renda = pl_bruto * 0.25
#         pl_liquido = pl_bruto - imposto_renda 

#     elif salario_float > 1000:
#         pl_bruto = (salario_float * 0.30) 
#         imposto_renda = pl_bruto * 0.25
#         pl_liquido = pl_bruto - imposto_renda
        
#     print(f'''
# o cálculo com base no salário do empregado {nome} é
# PL BRUTO         =    {pl_bruto:,.2f}
# Imposto De Renda =    {imposto_renda:,.2f}
# PL Liquido       =    {pl_liquido:,.2f}
# ''')
    
#     sair = input('você deseja sair? [s] ou [n]: ').lower().startswith('s')
    
#     if sair:
#         print('saindo.')
#         break

#     elif not sair:
#         print('Ok, continuando.')
#         continue
 
""" Exercicio-8

Faça um programa que leia o nome e a altura (em metros) de uma pessoa e
calcule e imprima os pesos mínimo e máximo para que ela esteja dentro
da faixa de peso ideal de acordo com a tabela de IMC (Índice de Massa Corporal) abaixo.

IMC = Peso / Altura2

IMC menor que 20  pessoa está abaixo do peso
IMC entre 20 e 25  pessoa está no peso ideal
IMC maior que 25  pessoa está acima do peso
"""

# nome = input('digite seu nome: ')
# altura = input('qual sua altura? em metros: ')

# altura_float = 0
# peso_float = 0
# flag = None
# imc_min = 20 
# imc_max = 25

# try:
#     altura_float = float(altura)
#     imc_min = 20 * altura_float ** 2
#     imc_max = 25 * altura_float ** 2
#     flag = True
# except:
#     flag = None
#     print('Valor Inválido, por favor digite novamente.')


# print(f'''
# a faixa de peso ideal para {nome} é:
# peso mínimo = {imc_min:.1f}
# peso máximo = {imc_max:.1f}
# ''')

"""
exercicio - 9
Tendo como dados de entrada a altura (em metros) e o sexo de uma pessoa
(“F” para feminino e “M” para masculino), faça um programa que calcule o peso ideal
da mesma, utilizando as seguintes fórmulas

Para homens: Peso Ideal = 62.1 * altura - 44.7
Para mulheres: Peso Ideal = 72.7 * altura - 58
"""

# altura = input('digite sua altura em metros: ')
# sexo = input('digite o seu sexo: [F] ou [M] ').lower()

# altura_float = 0
# sexo = sexo
# valor_valido = None
# peso_ideal_m = 0
# peso_ideal_f = 0

# try:   
#     altura_float = float(altura)
#     valor_valido = True
# except:
#     valor_valido = None
#     print('''
# você digitou a altura de forma inválida,
# por favor corrija usando sua altura em metros.
# ''')
#     exit()

# if sexo.startswith('f'):
#     peso_ideal_f = (62.1 * altura_float) - 44.7
#     print(f'o peso ideal para você é {peso_ideal_f:.3f}')

# elif sexo.startswith('m'):
#     peso_ideal_m = (72.7 * altura_float) - 58
#     print(f'o peso ideal para você é {peso_ideal_m:.3f}')


"""
Exercicio - 10

Ao se fazer uma determinada aplicação financeira, quando resgatamos o dinheiro,
a financeira calcula o valor a ser resgatado levando-se em conta o número de dias
que o dinheiro ficou aplicado, a taxa de juros diária, uma taxa de administração de
R$10,00 e o valor a ser retido na fonte de imposto de renda (percentual de 15%).
Faça um programa que calcule o valor resgatado, solicitando ao usuário o capital aplicado,
o número de dias que ficou aplicado e a taxa diária e calcule e imprime o rendimento,
o imposto de renda e o valor a ser resgatado

Rendimento = Capital Aplicado  x  Taxa Diária  x  Número de Dias
Imposto de Renda = 15%  sobre o Rendimento 
Valor Resgatado = Capital Aplicado + Rendimento - IR - Taxa de Administração

Observação: A Taxa Diária é informada percentualmente pelo usuário mas
deve ser convertida para ser utilizada na fórmula do cálculo do rendimento.
"""
# import os
# TAXA_ADMINISTRACAO = 10

# capital_str = input('nos diga o capital investido: ')
# taxa_diaria_str = input('nos diga a taxa diária: ')
# num_dias_str = input('quantos dias ficou investido o capital: ')

# imposto_renda = 0
# valor_resgatado = 0
# capital_float = 0
# num_dias_float = 0
# taxa_diaria_float = 0
# valor_valido = False

# try:
#     capital_float = float(capital_str)
#     num_dias_float = float(num_dias_str)
#     taxa_diaria_float = float(taxa_diaria_str) / 100
#     valor_valido = True
# except:
#     valor_valido = None
#     print('Valor Inválido. Digite apenas números.')

# if valor_valido:
#     rendimento = capital_float * taxa_diaria_float * num_dias_float
#     imposto_renda = rendimento * 0.15
#     valor_resgatado = capital_float + rendimento - imposto_renda - TAXA_ADMINISTRACAO


# os.system('cls')
# print(f'''
#       o valor do rendimento foi             =       {rendimento}
#       o valor do imposto de renda foi       =       {imposto_renda}
#       o valor resgatado foi                 =       {valor_resgatado:,.2f}''')
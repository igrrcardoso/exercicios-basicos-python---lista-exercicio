"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que
os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que
o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao 
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
"""

valor_horas = int(input('Quanto você recebe por hora? '))
horas_trabalhadas = int(input('Quais são as horas trabalhadas mensais? '))


salario_bruto = valor_horas * horas_trabalhadas
INSS = (salario_bruto * 10) / 100
fgts = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 3) / 100
CINCO_POR_CENTO = (salario_bruto * 5) / 100
DEZ_POR_CENTO = (salario_bruto * 10) / 100
VINTE_POR_CENTO = (salario_bruto * 20) / 100

if salario_bruto <= 900:
    print(f'''
          Salário Bruto: {valor_horas}*{horas_trabalhadas}                             : R$ {salario_bruto}
          (-) IR (0%)                                        : R$ 0
          (-) INSS (10%)                                     : R$ {INSS}
          FGTS(11%)                                          : R$ {fgts}
          Total Descontos                                    : R$ {INSS}
          Salário Liquido                                    : R$ {salario_bruto}''')
elif salario_bruto <= 1500:
     print(f'''
          Salário Bruto: {valor_horas}*{horas_trabalhadas}                          : R$ {salario_bruto}
          (-) IR (5%)                                        : R$ {CINCO_POR_CENTO}
          (-) INSS (10%)                                     : R$ {INSS}
          FGTS(11%)                                          : R$ {fgts}
          Total Descontos                                    : R$ {CINCO_POR_CENTO + INSS}
          Salário Liquido                                    : R$ {(salario_bruto - CINCO_POR_CENTO) - INSS}''')
elif salario_bruto <= 2500:
     print(f'''
          Salário Bruto: {valor_horas}*{horas_trabalhadas}                          : R$ {salario_bruto}
          (-) IR (10%)                                       : R$ {DEZ_POR_CENTO}
          (-) INSS (10%)                                     : R$ {INSS}
          FGTS(11%)                                          : R$ {fgts}
          Total Descontos                                    : R$ {DEZ_POR_CENTO + INSS}
          Salário Liquido                                    : R$ {(salario_bruto - DEZ_POR_CENTO) - INSS}''')
else:
     print(f'''
          Salário Bruto  {valor_horas}*{horas_trabalhadas}                          : R$ {salario_bruto}
          (-) IR (20%)                                       : R$ {VINTE_POR_CENTO}
          (-) INSS (10%)                                     : R$ {INSS}
          FGTS(11%)                                          : R$ {fgts}
          Total Descontos                                    : R$ {VINTE_POR_CENTO + INSS}
          Salário Liquido                                    : R$ {(salario_bruto - VINTE_POR_CENTO) - INSS}''')
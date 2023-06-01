"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input('Qual o seu salário? '))

# setando variavel salarios

SALARIO_280 = salario <= 280
SALARIO_280_700 = salario > 280 and salario <= 700
SALARIO_700_1500 = salario > 700 and salario <= 1500
SALARIO_1500 = salario > 1500

# porcentagens

vinte_porcento = (salario * 20) / 100
quinze_porcento = (salario * 15) / 100
dez_porcento = (salario * 10) / 100
cinco_porcento = (salario * 5) / 100

# aplicar ajustes aos salarios

salario_280_depois_reajuste = vinte_porcento + salario
salario_280_700_dps_reajuste = quinze_porcento + salario
salario_700_1500_dps_reajuste = dez_porcento + salario
salario_1500_dps_reajuste = cinco_porcento + salario


# percentual

percentual_280 = ((salario_280_depois_reajuste - salario) / salario) * 100

percentual_280_700 = ((salario_280_700_dps_reajuste - salario) / salario) * 100

percentual_700_1500 = ((salario_700_1500_dps_reajuste - salario) / salario) * 100

percentual_1500 = ((salario_1500_dps_reajuste - salario) / salario) * 100

# blocos if

#se o salario for igual ou menor que 280

if SALARIO_280:
    print(f'''
salario antes do reajuste: R$ {salario}
o aumento percentual foi: {percentual_280:.2f}%
o valor do aumento foi: R$ {vinte_porcento}
seu novo salario é: R$ {salario_280_depois_reajuste}
''')

# se o salario for maior que 280 e menor que 700    
elif SALARIO_280_700:
    print(f'''
salario antes do reajuste: R$ {salario}
o aumento percentual foi: R$ {percentual_280_700:.2f}%
o valor do aumento foi: R$ {quinze_porcento}
seu novo salario é: R$ {salario_280_700_dps_reajuste}
    ''')
elif SALARIO_700_1500:
    print(f'''
salario antes do reajuste: {salario}
o aumento percentual foi de {percentual_700_1500:.2f}%
o valor do aumento foi: {dez_porcento}
seu novo salario é: {salario_700_1500_dps_reajuste}
    ''')
else:
    print(f'''
salario antes do reajuste: {salario}
o aumento percentual foi de {percentual_1500:.2f}%
o valor do aumento foi: {cinco_porcento}
seu novo salario é: {salario_1500_dps_reajuste}
    ''')
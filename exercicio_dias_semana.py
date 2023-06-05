# Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido

dia_semana = int(input 
('''Digite o dia da semana.
ex: "1 = Segunda".
: '''))

if dia_semana == 1:
   dia_semana = "segunda"
elif dia_semana == 2:
   dia_semana = "terca"
elif dia_semana == 3:
    dia_semana = "quarta"
elif dia_semana == 4:
   dia_semana = "quinta"
elif dia_semana == 5:
   dia_semana = "sexta"
elif dia_semana == 6:
   dia_semana = "sabado"
elif dia_semana == 7:
   dia_semana = "domingo"
else:
    print('valor inválido')

print(dia_semana)
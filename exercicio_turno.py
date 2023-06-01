"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

horario = input('Em qual turno você estuda? [M]atutino [V]espertino ou [N]oturno: ')


if horario == 'm':
    print('Bom Dia!')
if horario == 'v':
    print('Boa Tarde!')
if horario == 'n':
    print('Boa Noite!')
if horario not in 'm' 'v' 'n':
    print('Valor Inválido!')
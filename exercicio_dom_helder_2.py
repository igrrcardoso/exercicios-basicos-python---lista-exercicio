""" Pelas regras da CBV, a pontuação que as equipes de vôlei ganham
ao fim de uma partida da Super Liga são: placares de 3 a 0 ou 3 a 1,
dão 3 pontos a equipe vencedora e nenhum ponto a equipe perdedora;
placar de 3 a 2, dão 2 pontos a equipe vencedora e 1 ponto a equipe perdedora.
Faça um programa que leia os nomes das equipes (equipe 1 e equipe 2)
e o placar de um jogo (sets ganhos da equipe 1 e sets ganhos da equipe 2),
e calcule e imprima os pontuação que cada equipe ganhou na partida.


    Equipe 1 = Cruzeiro	Equipe 2 = Minas
    Sets  equipe 1 = 2	Sets  equipe 2 = 3
    Pontos Cruzeiro = 1	Pontos Minas = 2
Para testar:
    Equipe 1 = Taubaté	Equipe 2 = Osasco
    Sets  equipe 1 = 3	Sets  equipe 2 = 0
Pontos Taubaté = 3	Pontos Osasco = 0
"""

# equipe1 = input('Qual o nome da primeira equipe: ')
# sets_equipe1 = input(f'Quantos sets a equipe {equipe1} ganhou: ')
# equipe2 = input('Qual o nome da segunda equipe: ')
# sets_equipe2 = input(f'Quantos sets a equipe {equipe2} ganhou: ')

# valor_invalido = False
# pontos_equipe1 = 0
# pontos_equipe2 = 0
# set_equipe1_int = 0
# set_equipe2_int = 0

# try:
#     set_equipe1_int = int(sets_equipe1)
#     set_equipe2_int = int(sets_equipe2)
#     valor_invalido = True
# except:
#     print('Valor Inválido, favor digitar apenas números nos sets.')
#     valor_invalido = False

# if set_equipe1_int == 3 and set_equipe2_int <= 1:
#     pontos_equipe1 = 3
#     pontos_equipe2 = 0

# elif set_equipe1_int == 3 and set_equipe2_int == 2:
#     pontos_equipe1 = 2
#     pontos_equipe2 = 1

# elif sets_equipe2 == 3 and set_equipe1_int <= 1:
#     pontos_equipe2 = 3
#     pontos_equipe1 = 0

# elif set_equipe2_int == 3 and set_equipe1_int == 2:
#     pontos_equipe2 = 2
#     pontos_equipe1 = 1

# os.system('cls')

# print(f'''
# Equipe 1 = {equipe1}      Equipe 2 = {equipe2}
# Sets Equipe 1 = {sets_equipe1}       Sets Equipe2 = {sets_equipe2}
# Pontos {equipe1} = {pontos_equipe1}      Pontos {equipe2} = {pontos_equipe2}
#       ''')

"""
Exercício - 12
Uma indústria produtora de  bolas de futebol fabricou uma grande quantidade
para vender na época da Copa do Mundo em 2018. Para isto ela deverá estocar
toda a produção em galpões a serem alugados até a Copa.
As bolas serão armazenadas em caixas de papelão, que comportam até 10 bolas.
Cada galpão a ser alugado comporta até 850 caixas de papelão.
Faça um programa que leia a quantidade de bolas produzidas pela fábrica,
a quantidade de bolas com defeito e que serão descartadas,
o preço unitário das caixas de papelão, a quantidade de meses até a Copa,
além do valor mensal do aluguel, e calcule e imprima o custo total de embalagem
mais custo total de estocagem de toda a produção.

Observação: A última caixa de papelão deverá ser estocada mesmo que incompleta.
O último galpão deverá ser alugado mesmo que não esteja totalmente cheio.
"""

# qtd_produzida = float(input('Quantas bolas foram produzidas: '))
# qtd_descarte = float(input('Quantas bolas serão descartadas: '))
# valor_papelao = float(input('Qual o valor da caixa de papelão(Unidade): '))
# valor_aluguel = float(input('Qual o valor do aluguel mensal dos galpões: '))
# meses = float(input('Quantos meses até a copa: '))

# # Caixas necessárias
# total_bolas = qtd_produzida - qtd_descarte
# quantidade_caixas = math.ceil(total_bolas / 10)
# # quantidade galpões necessários
# galpão = math.ceil(quantidade_caixas / 850)
# # Custos
# custo_estocagem = valor_aluguel * meses
# custo_caixas = quantidade_caixas * valor_papelao
# # Custo total
# total = galpão * valor_aluguel * meses

# print(f'a quantidade de caixas necessárias serão: {quantidade_caixas}')
# print(f'o custo de todas as caixas serão: R${custo_caixas:,.2f}')
# print(f'o custo de estocagem será: R${custo_estocagem:,.2f}')
# print(f'o custo total será R${custo_caixas + total:,.2f}')

"""
Exercicio - 13
Faça um programa que leia a hora inicial, minuto inicial,
hora final e minuto final de um jogo
(cada valor em uma variável do tipo inteiro diferente).
A seguir, calcule e imprima a duração do jogo,
mostrando o resultado no seguinte formato:

“O jogo durou xxx horas e yyy minutos”.

Observação: O jogo terminou no mesmo dia em que ele começou.
"""

# hora_inicial = input('Hora inicial do jogo: ')
# minuto_inicial = input('Minuto inicial: ')
# hora_final = input('Hora final do jogo: ')
# minuto_final = input('Minuto final do jogo: ')

# flag = False
# hora_total = 0
# minuto_total = 0

# if ':' in hora_inicial:
#     print(
#         'Você digitou ":" provavelmente para separar a hora dos minutos.'
#         'Por favor digite o horário em seu respectivo campo.'
#         'Assim como os minutos.'
#           )

# try:
#     hora_inicial_int = int(hora_inicial)
#     minuto_inicial_int = int(minuto_inicial)
#     hora_final_int = int(hora_final)
#     minuto_final_int = int(minuto_final)
#     hora_total = hora_final_int - hora_inicial_int
#     minuto_total = minuto_final_int - minuto_inicial_int
#     flag = True

#     if minuto_total < 0:
#         hora_total -= 1
#         minuto_total += 60
# except:
#     flag = False
#     print('Valor Inválido, favor digitar apenas números.')

# print(f'o jogo durou {hora_total} Horas e {minuto_total} Minutos.')

"""
Exercicio - 14
Faça um programa que leia um número inteiro de 4 dígitos,
e o imprima de trás para frente. Antes de imprimir o número de forma invertida
verifique se ele realmente tem 4 dígitos,
senão informar “NÚMERO TEM QUE TER 4 DÍGITOS”
"""

# numero_input = input('digite um número de 4 dígitos: ')

# numero_inverso = numero_input

# if len(numero_input) >= 4:
#     numero_inverso = numero_input[::-1]
# else:
#     print('NÚMERO TEM QUE TER 4 DÍGITOS')
#     exit()

# print(numero_inverso)

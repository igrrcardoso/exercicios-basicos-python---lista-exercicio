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

"""
Uma operadora de TV a cabo nacional oferece uma série de serviços aos seus
assinantes. A conta a ser paga por um assinante, no fim do mês,
é constituída por um valor fixo mensal somado ao consumo dos canais
pay-per-view, que são cobrados por uso diário,
ambos de acordo com o pacote que ele contratou (ver tabela 1),
mais os serviços extras, além da cobrança dos impostos sobre os serviços
prestados que varia conforme a cidade do assinante (ver tabela 2).

Faça um programa que solicite ao usuário o código do seu pacote,
a quantidade de dias de consumo de canais pay-per-view,
o valor dos serviços extras, e a cidade do assinante,
e calcule e imprima o valor da conta que o assinante deverá pagar.

Conta = Valor Fixo + Diárias Canais PPP + Serviços Extras + Imposto
(sobre Fixo/PPP/Extras)
"""

# # inputs
# codigo_input = input('qual o código da sua assinatura [1] [2] [3]: ')
# diaria_input = input('quantos dias de consumo em canais PPP: ')
# extras_input = input('qual o valor dos serviços extras: ')
# cidade_input = input(
#     'você é de qual cidade?'
#     '[BH] [SP] [RJ] [OU]tras cidades: '
# ).upper()

# # set variáveis.
# valor_fixo = 0
# diaria = 0
# imposto = 0
# diaria_float = 0
# extras_float = 0

# # conversão str para float.
# try:
#     diaria_float = float(diaria_input)
#     extras_float = float(extras_input)

# # verificando oque foi digitado no input cidade.
#     if cidade_input not in ["BH", "SP", "RJ", "OU"]:
#         print(
#             'Valor Inválido.\nDigite a cidade novamente '
#             'usando o guia:\n'
#             'BH = Belo Horizonte\n'
#             'SP = São Paulo\n'
#             'RJ = Rio De Janeiro\n'
#             'OU = Outras Cidades\n'
#             )

# # verificando oque foi digitado no input codigo.
#     elif len(codigo_input) > 1:
#         print(
#             f'!Erro!\nO Erro está em Código: "{codigo_input}", para corrigir:'
#             '\n'
#             'Digite um código por vez.'
#             )
#     elif codigo_input not in ["1", "2", "3"]:
#         print(
#             f'!Erro!\nO Erro está em Código: "{codigo_input}", para corrigir:'
#             '\n'
#             'Digite um plano válido.\n'
#             'Planos Válidos = [1]Basic, [2]Advanced, [3]Master'
#             )
#         exit()

# # calculando valor da diária e setando valor fixo para cada cidade.
#     elif codigo_input == '1':
#         valor_fixo = 65
#         valor_máximo = 65
#         diaria = min(diaria_float * 1.20, valor_máximo)
#     elif codigo_input == '2':
#         valor_fixo = 104
#         diaria = diaria_float * 2.10
#     elif codigo_input == '3':
#         valor_fixo = 137

# # setando valor de imposto para cada cidade.
#     if cidade_input == 'BH':
#         imposto = 0
#     elif cidade_input == 'SP':
#         imposto = 0.01
#     elif cidade_input == 'RJ':
#         imposto = 0.015
#     else:
#         imposto = 0.2

# # calculando o valor total da conta e exibindo na tela.
#     valor_total = (valor_fixo + diaria + extras_float) * (1 + imposto)
#     print(f'Valor Total da conta = {valor_total:,.2f}')
# except ValueError:
#     print(
#         'Erro no código.\n'
#         f'O erro está em "{diaria_input}" ou em "{extras_input}" \n'
#         'Para corrigir você deve digitar apenas números nestas linhas.'
#     )

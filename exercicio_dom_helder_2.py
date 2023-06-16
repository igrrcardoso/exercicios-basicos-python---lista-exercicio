import os

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
Exercicio - 15
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
#             f'!Erro!\nO Erro está no Código: "{codigo_input}",para corrigir:'
#             '\n'
#             'Digite um código por vez.'
#             )
#     elif codigo_input not in ["1", "2", "3"]:
#         print(
#             f'!Erro!\nO Erro está no Código: "{codigo_input}",para corrigir:'
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

"""
Exercicio - 16
Uma escola de línguas tem uma fórmula bem peculiar para calcular
o RESULTADO FINAL de seus alunos. Ela leva em conta o número de faltas,
as três notas de provas, a nota do trabalho final e a idade do aluno.
Faça um programa para ler as faltas, as notas das provas,
a nota do trabalho final e a idade do aluno,
e que calcule e imprima o seu resultado final.

Nota Final = Média aritmética das duas maiores
Notas das Provas X Peso1 + Nota do Trabalho Final X Peso2
"""
# Inputs
# nome = input('Qual é seu nome: ')
# faltas = input('quantas faltas você teve: ')
# prova1 = input('nota da primeira prova: ')
# prova2 = input('nota da segunda prova: ')
# prova3 = input('nota da terceira prova: ')
# trabalho = input('nota do trabalho final: ')
# idade = input('qual sua idade: ')

# # Set Variáveis
# flag = False
# erro = False
# peso1 = 1
# peso2 = 1
# nota_final = 0
# media = 0
# resultado = 'reprovado'
# # Bloco try converter variáveis e verificar erros de entrada.
# try:
#     faltas_int = int(faltas)
#     prova1_float = float(prova1)
#     prova2_float = float(prova2)
#     prova3_float = float(prova3)
#     trabalho_float = float(trabalho)
#     idade_int = int(idade)
#     flag = True

#     try:
#         if nome.isdigit():
#             raise ValueError(
#                 '!ERRO!\n'
#                 'Use somente letras no nome.'
#                 )
#         elif nome.strip() == '':
#             raise ValueError(
#                 '!ERRO!\n'
#                 'Nome vazio'
#                 )
#     except ValueError as ve:
#         os.system('cls')
#         print(ve)
#         exit()

# except ValueError:
#     if flag is False:
#         os.system('cls')
#         print(
#             '!ERRO!\n'
#             'Você colocou letras no lugar de números em algum dos campos\n'
#             'Por Favor, coloque apenas dígitos nestes campos.')
#     exit()

# # bloco if para ver qual as duas maiores provas.
# if prova1_float > prova2_float and prova1_float < prova3_float:
#     media = (prova1_float + prova3_float) / 2
# elif prova1_float > prova3_float and prova1_float < prova2_float:
#     media = (prova1_float + prova2_float) / 2
# elif prova2_float > prova1_float and prova2_float < prova3_float:
#     media = (prova2_float + prova3_float) / 2
# elif prova2_float > prova3_float and prova2_float < prova1_float:
#     media = (prova2_float + prova1_float) / 2
# elif prova3_float > prova2_float and prova3_float < prova1_float:
#     media = (prova3_float + prova1_float) / 2
# else:
#     media = (prova3_float + prova2_float) / 2

# # bloco if para ver qual será o peso1 dependendo das faltas
# if faltas_int <= 5:
#     peso1 = 3
# elif faltas_int > 5 and faltas_int <= 10:
#     peso1 = 2
# else:
#     peso1

# # bloco if para ver qual será o peso2 dependendo da idade
# if idade_int <= 17:
#     peso2
# elif idade_int > 17 and idade_int <= 50:
#     peso2 = 2
# else:
#     peso2 = 3

# # calculo da nota final
# nota_final = (media * peso1) + (trabalho_float * peso2)

# # mostrando a nota final como Reprovado, Regular, Bom, Muito Bom ou Excelente
# if nota_final <= 50:
#     nota_final = 'Ruim'
#     resultado = 'Reprovado'
# elif nota_final > 50 and nota_final <= 70:
#     nota_final = 'Regular'
#     resultado = 'Aprovado'
# elif nota_final > 70 and nota_final <= 80:
#     nota_final = 'Bom'
#     resultado = 'Aprovado'
# elif nota_final > 80 and nota_final <= 90:
#     nota_final = 'Muito Bom'
#     resultado = 'Aprovado'
# else:
#     nota_final = 'Excelente'
#     resultado = 'Aprovado'

# os.system('cls')
# print(
#     f'{nome.capitalize()},\n'
#     f'Sua nota final foi: {nota_final}\n'
#     f'E você está: {resultado}')

"""
Exercicio - 1 (switch)
Faça um programa que leia o número referente a algum mês do ano,
e imprima a que trimestre ele pertence.

Meses       Trimestre
1,2 e 3     1º
4,5 e 6     2º
7,8 e 9     3º
10,11 e 12  4º
"""


# def verificar_trimestre(mes_do_ano):
#     if mes_do_ano in ['1', '2', '3']:
#         return '1º Trimestre'
#     elif mes_do_ano in ['4', '5', '6']:
#         return '2º Trimestre'
#     elif mes_do_ano in ['7', '8', '9']:
#         return '3º Trimestre'
#     else:
#         return '4º Trimestre'


# mes_do_ano = input('Qual o mês do ano: ')
# trimestre = verificar_trimestre(mes_do_ano)
# print(
#     f'Você está no {mes_do_ano}º mês do ano.\n'
#     f'que é referente ao {trimestre}'
# )

"""
Exercicio - 2 Switch
Faça um programa que leia as 3 notas parciais de um aluno
(valores inteiros entre 0 e 10), calcule a NOTA FINAL
(média inteira das notas parciais)
e imprima o CONCEITO do aluno conforme a tabela abaixo:

Nota final:         Conceito:
9 ou 10             A
8                   B
7                   C
5 ou 6              D
1,2,3 e 4           E

"""

# nota_parcial_1 = input('Primeira nota: ')
# nota_parcial_2 = input('Segunda nota: ')
# nota_parcial_3 = input('Terceira nota: ')

# flag = True
# media = 0
# conceito = 'A'

# try:
#     nota1_int = int(nota_parcial_1)
#     nota2_int = int(nota_parcial_2)
#     nota3_int = int(nota_parcial_3)
#     media = round(nota1_int + nota2_int + nota3_int) // 3
#     flag = False
# except ValueError:
#     if flag:
#         exit()

# if media >= 9:
#     conceito = 'A'
# elif media >= 8:
#     conceito = 'B'
# elif media >= 7:
#     conceito = 'C'
# elif media >= 5 and media <= 6:
#     conceito = 'D'
# else:
#     conceito = 'E'

# print(f'O conceito final com base em suas notas é: "{conceito}"')


"""
Exercicio - 3 / Switch
"""

# valor_imposto = input('Valor da multa: ')
# dias_atraso = input('Dias de atraso: ')

# erro = True
# percentual_imposto = 0
# percentual_dias_atraso = 0
# total = 0

# try:
#     valor_imposto_float = float(valor_imposto)
#     dias_atraso_float = float(dias_atraso)
#     erro = False
# except ValueError as ve:
#     if erro:
#         print('Erro', ve)
#         exit()

# if dias_atraso_float >= 5:
#     percentual_imposto = 0
# elif dias_atraso_float > 6 and dias_atraso_float <= 8:
#     percentual_imposto = valor_imposto_float * 0.02
# elif dias_atraso_float > 9 and dias_atraso_float <= 10:
#     percentual_imposto = valor_imposto_float * 0.1
#     percentual_dias_atraso = dias_atraso_float * 0.05
# else:
#     percentual_imposto = valor_imposto_float * 1.5
#     for dia in range(1, dias_atraso + 1):
#         total += 1

# print(percentual_imposto, total)

"""
Exercicio - 4 / Switch
Uma loteria esportiva paga prêmios proporcionais
a quantidade de acertos de cada apostador.
Ela tem 13 jogos. Se o apostador acertar até 5 jogos ele não ganha nada,
se acertar de 6 a 10 jogos ele ganha um outro cartão para apostar,
se acertar 11 jogos ganha R$100, 12 jogos R$1000 e 13 jogos R$50000.
Faça um programa que leia o nome do apostador e a quantidade de jogos
que ele acertou, e calcule e imprima o prêmio que ele ganhou.

Acertos                           Prêmio

Até 5                             Nenhum
De 6 até 10                       Outro Cartão
11                                R$100,00
12                                R$1.000,00
13                                R$50.000,00

Para testar:
4 acertos -> Nenhum prêmio
7 acertos -> Ganha outro cartão
13 acertos -> Prêmio de 50.000,00
"""

while True:
    nome = input('nos diga seu nome: ')
    acertos = input('diga a quantidade de jogos acertados: ')

    premio_str2 = ''
    premio_str1 = ''
    premio = 0

    try:
        acertos_int = int(acertos)

        if nome.isdigit():
            raise ValueError('!Erro!\nSeu nome não pode ser um digito.')
        elif not acertos.isdigit():
            raise ValueError('!Erro!\n Jogos acertados precisa ser um digito.')
        elif acertos_int > 13:
            raise ValueError('!Erro!\n Número máximo de acertos é 13.')

        if acertos_int <= 5:
            premio_str1 = 'Nenhum prêmio.'
        elif acertos_int >= 6 and acertos_int <= 10:
            premio_str2 = 'Você ganhou outro cartão para apostar.'
        elif acertos_int == 11:
            premio = 100
        elif acertos_int == 12:
            premio = 1000
        else:
            premio = 50000

        if premio_str1:
            print(f'{nome.capitalize()}, você não ganhou {premio_str1}')
        elif premio_str2:
            print(f'Parabéns {nome.capitalize()}, {premio_str2}')
        elif premio:
            print(f'Parabéns {nome.capitalize()}, você ganhou {premio:,.2f}')

        sair = input('Você deseja sair? [S]im ou [N]ão: ').lower()

        if sair == 's':
            print('Saindo...')
            exit()
        else:
            print('Continuando...')
            os.system('cls')
            continue

    except ValueError as ve:
        if 'invalid literal for int() with base 10' in str(ve):
            print('Valor Inválido\nOs acertos precisam ser números inteiros')
        else:
            print(ve)
        continue

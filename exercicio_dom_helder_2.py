import os

"""
Pelas regras da CBV, a pontuação que as equipes de vôlei ganham
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

equipe1 = input('Qual o nome da primeira equipe: ')
sets_equipe1 = input(f'Quantos sets a equipe {equipe1} ganhou: ')
equipe2 = input('Qual o nome da segunda equipe: ')
sets_equipe2 = input(f'Quantos sets a equipe {equipe2} ganhou: ')

valor_invalido = False
pontos_equipe1 = 0
pontos_equipe2 = 0
set_equipe1_int = 0
set_equipe2_int = 0

try:
    set_equipe1_int = int(sets_equipe1)
    set_equipe2_int = int(sets_equipe2)
    valor_invalido = True
except:
    print('Valor Inválido, favor digitar apenas números nos sets.')
    valor_invalido = False

if set_equipe1_int == 3 and set_equipe2_int <= 1:
    pontos_equipe1 = 3
    pontos_equipe2 = 0

elif set_equipe1_int == 3 and set_equipe2_int == 2:
    pontos_equipe1 = 2
    pontos_equipe2 = 1

elif sets_equipe2 == 3 and set_equipe1_int <= 1:
    pontos_equipe2 = 3
    pontos_equipe1 = 0

elif set_equipe2_int == 3 and set_equipe1_int == 2:
    pontos_equipe2 = 2
    pontos_equipe1 = 1

os.system('cls')

print(f'''
Equipe 1 = {equipe1}      Equipe 2 = {equipe2}
Sets Equipe 1 = {sets_equipe1}       Sets Equipe2 = {sets_equipe2}
Pontos {equipe1} = {pontos_equipe1}      Pontos {equipe2} = {pontos_equipe2}
      ''')

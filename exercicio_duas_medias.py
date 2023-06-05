"""
 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
 ao longo de um semestre, e calcule a sua média.
 A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  """

nome = input('Qual seu nome? ')
primeira_media = float(input('Qual a primeira nota? '))
segunda_media = float(input('Qual a segunda nota? '))

media = (primeira_media + segunda_media) / 2

if media >= 9:
    nota = "A"
elif media >= 7.5 and media <= 9:
    nota = "B"
elif media >= 6.0 and media <= 7.5:
    nota = "C"
elif media >= 4.0 and media <= 6.0:
    nota = "D"
elif media >= 4.0 and media <= 0:
    nota = "E"

if nota == "D" or nota == "E":
    print(f'''
          {nome}, você foi REPROVADO 
          Media  : {media}
          Nota   : {nota}
          ''')
else:
    print(f'''
        {nome}, você foi APROVADO
        Media  : {media}
        Nota   : {nota}
        ''')
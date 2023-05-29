# Instrução calculadora de peso

print('''
    para calcular seu peso, especifique sua altura em
    centimetros no campo abaixo
    exemplo: 1,80m = 180cm
    ''')

# input para saber o gênero
sexo = input('Você é [H]omem ou [M]ulher? ')

# bloco calculadora peso masculino
if sexo in 'h' 'H':
    altura_h = int(input('Digite a sua altura em "cm" : '))
    converter_altura = altura_h / 100
    peso_ideal_h = (72.7*converter_altura) - 58
    print(f'o seu peso ideal é: {peso_ideal_h:.1f}Kg')

# bloco calculadora peso feminino
elif sexo in 'm' 'M':
    altura_m = int(input('digite sua altura em "cm": '))
    converter_altura = altura_m / 100
    peso_ideal_m = (62.1*converter_altura) - 44.7
    print(f'seu peso ideal é: {peso_ideal_m:.1f}')

# em caso de nada ser digitado no primeiro input
else:
    print('Você não inseriu seu gênero, favor digita-lo usando "H" ou "M".')

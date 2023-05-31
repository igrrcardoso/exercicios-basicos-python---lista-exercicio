# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

verificar = input('digite uma letra : ')

if verificar in 'A' 'a' 'e' 'E' 'i' 'I' 'o' 'O' 'u' 'U':
    print(f'{verificar} é uma vogal')
else:
    print(f'{verificar} é uma consoante')
    
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

verificar = input('digite uma letra : ').lower()

if verificar in 'a' 'e' 'i' 'o' 'u':
    print(f'{verificar} é uma vogal')
else:
    print(f'{verificar} é uma consoante')

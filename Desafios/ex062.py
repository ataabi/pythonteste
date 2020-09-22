# Melhore o DEFASIO061 ,perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar os termos.

p1 = int(input('Primeiro Termo: '))
r = int(input('Razão'))
ter = 1
count = 1
while count != 0:
    print(f'P{ter}:{p1} ',end=',')
    p1 += r
    ter += 1
    count += 1
    if count > 10:
        esc = input('\nDeseja continuar (S/N)').upper()
        if esc == 'N':
            count = 0
        else:
            count = 1


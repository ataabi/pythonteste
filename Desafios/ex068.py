# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('-=-'*10,)
print(f'''{'VAMOS JOGAR PAR OU IMPAR':^30}''')
print('-=-'*10)
from random import randint
pp = 0 #Player points
while True:
    ia = randint(0,10)

    esc = str(input('Você quer Par ou Impart (P/I): ')).strip().lower()
    while not esc in 'pi':
        esc = str(input('Você quer Par ou Impart (P/I): ')).strip().lower()

    while True:
        try:
            player = int(input('Escolha um número: '))
            break
        except:
            player = int(input('Escolha um número: '))

    r = (ia+player)%2
    if r == 0:
        print(f'{ia} + {player} = {ia+player} e {ia+player} é par')
        print('-=-' * 11)
    if r != 0:
        print(f'{ia} + {player} = {ia+player} e {ia+player} é impar')
        print('-=-' * 11)
    if 'p' in esc:
        if r == 0:
            print('Parabéns, Você acertou')
            pp += 1
        elif r != 0:
            print('A Vitória é minha')
            break
    elif 'i' in esc:
        if r != 0:
            print('Parabéns, Você acertou')
            pp += 1
        elif r == 0:
            print('A Vitória é minha')
            break
print(f'-=-'*11)
print(f'Resultado final, você ganhou {pp}x')
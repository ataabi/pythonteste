# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10,
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.
from random import randint
player = 0
count = 0
print('\033[4:35m-#\033[m'*20,
      f"\n{'[ Jogo de Adivinha ]':^40}",)
print('\033[4:35m-#\033[m'*20)
dif = str(input(F'{"Escolha a dificuldade":-^40}\n'
      '[F]-Fácil | [M]-Médium | [D]-Dificil : ')).strip().upper()
print('\033[4:35m-#\033[m'*20)

while dif not in 'FMD':
    dif = str(input('Comando invalido.\n'
                    '[F]-Fácil | [M]-Médium | [D]-Dificil |: '))
if dif == 'F':
    ia = randint(1,10)
    print('Pensei em um número entre 1 e 10')
elif dif == 'M':
    ia = randint(1,30)
    print('Pensei em um número entre 1 e 30')
elif dif == 'D':
    ia = randint(1,50)
    print('Pensei em um número entre 1 e 50')

while ia != player:
    player = int(input('Em que numero estou pensando ??? : '))
    count += 1
    if player != ia:
        print(f'Vixi, não é o {player},',end='')
    if ia < player:
        print('é um número menor')
    if ia > player:
        print('è um númeno maior')

print(f'Isso Mesmo. Eu estava pensando no {ia}\n'
      f'E você teve que tentar {count}x até acertar.')

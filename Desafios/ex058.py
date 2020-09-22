# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10,
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.
from random import randint
ia = randint(1,10)
player = 0
count = 0
print('\033[4:35m-#\033[m'*20,
      f"\n{'[ Jogo de Adivinha ]':^40}\n",
      '\033[4:35m-#\033[m'*20)
while ia != player:
    player = int(input('Em que numero estou pensando ??? \n: '))
    if player != ia:
        print(f'Vixi, não é o {player}, tenta de novo.')
    count += 1
print(f'Isso Mesmo. Eu estava pensando no {ia}\n'
      f'E você teve que tentar {count}x até acertar.')
if count > 5:
    print('\033[31mNOOB\033[m')

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final coloque esse dicionáio em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep

play = {}
print('§'*27)
sleep(0.5)

for c in range(1, 5):
    play[c] = randint(1, 6)
    print(f'§§§  Jogador {c} jogou {play[c]}  §§§')
    sleep(0.5)

print('§'*27)
sleep(1)
print(f"{'§ -Ranking dos Jogadores- §':24}")

for e, c in enumerate(sorted(play.items(), key=lambda play:play[1], reverse=True)):
    print(f'§§ {e+1}ª - jogador-{c[0]} com {c[1]}  §§')


print('§'*27)
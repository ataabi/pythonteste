# faça um programa que ajuda um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogo = []
print("-$-"*15)
print(f'{"Jogo Da MEGA SENA":^45}')
print("-$-"*15)

n = int(input('Quantos jogos quer gerar?: '))
for j in range(0,n):
    for c in range(0,6):
        jogo.append(randint(1,60))
        for v in jogo:
            if v in jogo:
                jogo[-1] = randint(1,60)
    jogo.sort()
    sleep(1)
    print(f'O jogo {(j+1)}ª é \033[4:32m{jogo}\033[m')
    jogo.clear()

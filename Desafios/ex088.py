# faça um programa que ajuda um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
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
        while jogo.count(v) >=2:
            jogo.remove(v)
            jogo.append(randint(1,60))
    jogo.sort()
    sleep(1)
    print(f'O jogo {(j+1)}ª é \033[4:32m{jogo}\033[m')
    jogo.clear()
'''
# Resposta
from random import randint
from time import sleep
lista = []
jogos = []
print("-$-"*15)
print(f'{"Jogo Da MEGA SENA":^45}')
print("-$-"*15)
esc = int(input("Quantos jogos você quer sortear ? "))
tot = 0

while (tot+1) <= esc:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print("-$-"*15)

print('-$-'*4,f'SORTEANDO{esc:^5}JOGOS','-$-'*4)
for e,c in enumerate(jogos):
    print(f'O {e+1} jogo é \033[4:32m{c}\033[m')
    sleep(1)
print("-$-"*15)

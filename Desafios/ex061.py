# Refaça o DESAFIO051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.

p1 = int(input('Primeiro Termo : '))
r = int(input('Razão'))
nt = 0
while nt != 10:
    print(f'P{nt+1}:({p1}), ',end='')
    p1 += r
    nt += 1
# Faça um programa que tenha uma função chamada contador(),que receba três parâmetros: inicio,fim e possa e realize
# contagem. Seu programa tem que realizer três contagems atravês da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) Uma contagem personalizada.
from time import sleep

def contador(i,f,p):
    print("~" * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if p == 0:
        p = 1
    if p < 0:
        p *=1
    if i < f:
        while cont <= f:
            sleep(0.4)
            print(f' {cont}',end='', flash=True)
            cont += p
    else:
        while cont >= f:
            sleep(0.4)
            print(f' {cont}',end='', flush=True)
            cont -= p
    print('. FIM')


contador(1,10,1)
contador(10,0,2)
print("~" * 30)
print('Agora é sua vez:')
i = int(input('Digite um valor para o Inicio: '))
f = int(input('Digite um valor para o Fim: '))
p = int(input('Digite um valor para a Razão'))
contador(i,f,p)

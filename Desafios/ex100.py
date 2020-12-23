# Faça um programa que tenha uma lista chama números e duas funções chamadas sorteia() e somapar().
# A primeira função vai sortear 5 números e ai coloálos dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(sorteio):
    print('=-' * 25)
    print('Gerando os valores da lista ... :>',end=' ')
    for c in range(0,5):
        sorteio.append(randint(0,10))
        print(sorteio[c],end=' '),sleep(0.5)
    print('<:')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares da lista {lista} é {soma}')
    print('=-'*25)

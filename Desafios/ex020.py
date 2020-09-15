# o mesmo professor do desafio anterior quer sortear o ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e motre a ordem sorteada
#deck = []
#r = 0
#while r != 4:
#    a = input('Digite o nome do Aluno: ')
#    r = r + 1
#    deck.append(a)
#shuffle(deck)
#
#print(deck)

import random
print('Digite abaixo o nome dos 4 alunos a gerem sorteados.')
a1 = 'Primeiro aluno.'
a2 = 'Segundo aluno.'
a3 = 'Terceiro aluno.'
a4 = 'Quarto aluno.'
deck = [ a1 , a2 , a3 , a4 ]
print(deck)
shu = deck.split
print(shu)
print(random.choices(shu))
#print(f'{sort[0]}{sort[1]}')
print()
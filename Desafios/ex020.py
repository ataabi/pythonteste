# o mesmo professor do desafio anterior quer sortear o ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e motre a ordem sorteada
from random import shuffle
print('Digite abaixo o nome dos 4 alunos a gerem sorteados.')
a1 = 'Primeiro aluno.'
a2 = 'Segundo aluno.'
a3 = 'Terceiro aluno.'
a4 = 'Quarto aluno.'
deck = [ a1 , a2 , a3 , a4 ]
shuffle(deck)
print(deck)
# o mesmo professor do desafio anterior quer sortear o ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e motre a ordem sorteada
from random import shuffle
deck = []
r = 0

while r != 4:
    a = input('Digite o nome do Aluno: ')
    r = r + 1
    deck.append(a)

shuffle(deck)
print(deck)
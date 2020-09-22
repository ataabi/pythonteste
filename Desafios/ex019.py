# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
print('Digite o nome dos alunos')
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
deck = [a1,a2,a3,a4]
print(f'{choice(deck)} é quem vai limpar o Quadro')


# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
print('Digite o nome dos alunos')
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
num = random.randint(1,4)
if num == 1:
    print(f'{a1} vai limpar o quadro')
if num == 2:
    print(f'{a2} vai limpar o quadro')
if num == 3:
    print(f'{a3} vai limpar o quadro')
if num == 4:
    print(f'{a4} vai limpar o quadro')

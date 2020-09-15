#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario venceu ou perdeu.
from random import randint
n = randint(0,5)
print("Jogo de Adivinhação")
print('-'*20)
print('Tente acertar o numero que esta na minha memoria \n'
      'Dica : É algo entre 0 e 5')
r = int(input('Qual é o número ?'))
if r == n:
    print(f'Ola só vc acertou, eu estava pensando no {n}')
else:
    print('Que pena vc errou , tente de novo.')
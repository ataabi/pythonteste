#Crie um programa que faça o computador jogar jokenpo com você.
from random import randint
ia = randint(1,3)
print(f"{'Jokenpo':^36}")
print(f'{"Para escolher digite:":^36}\n'
      '(1)- Pedra ,(2)- Papel,(3)- Tesoura')
user = int(input(f''))
dic = {1:'Pedra',2:'Papel',3:'Tesoura'}
print(f'{dic[user]} x {dic[ia]}')
if user == ia:
    print('Empate')
elif user == 1 and ia == 3:
    print('   You WIN')
elif user == 2 and ia == 1:
    print('   You WIN')
elif user == 3 and ia == 2:
    print('   You WIN')
else:
    print('   You Lose')
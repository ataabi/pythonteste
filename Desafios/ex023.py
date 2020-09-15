#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#EX: Digite um numero: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1
n = input('Digite um numero entre 0 e 9999 \n: ')
if len(n) == 1:
    print(f'Unidade:{n[0]}')
if len(n) == 2:
    print(f'Unidade:{n[1]}\nDezena:{n[0]}')
if len(n) == 3:
    print(f'Unidade:{n[2]}\nDezena:{n[1]}\nCentena:{n[0]}')
if len(n) == 4:
    print(f'Unidade:{n[3]}\nDezena:{n[2]}\nCentena:{n[1]}\nMilhar:{n[0]}')
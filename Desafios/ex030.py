#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.
n = int(input('Digite um numero :'))
check = (n%2)
if check == 0:
    print('Esse numero é PAR')
else:
    print('Esse numero é IMPAR')
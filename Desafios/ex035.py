#Desenvola um programa que leia o comprimento de tres retas e diga ao usuario
# se elas podem ou nao formar um triangulo.
r1 = int(input('Digite o valor da 1° Reta. \n:'))
r2 = int(input('Digite o Valor da 2° Reta. \n:'))
r3 = int(input('Digite o valor da 3° Reta \n:'))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Essas Retas formam um Triangulo')
else:
    print('Essas Retas nao formam um Triangulo')

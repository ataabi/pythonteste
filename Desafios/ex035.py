#Desenvola um programa que leia o comprimento de tres retas e diga ao usuario
# se elas podem ou nao formar um triangulo.
print('Essas Retas fomam um triângulo ?')
r1 = float(input('Digite o valor da 1° Reta.: '))
r2 = float(input('Digite o Valor da 2° Reta.: '))
r3 = float(input('Digite o valor da 3° Reta.: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Essas Retas FORMAM um Triangulo')
else:
    print('Essas Retas nao FORMAM um Triangulo')

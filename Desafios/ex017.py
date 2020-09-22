# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
ad = float(input('Digite o cateto adjacente: '))
op = float(input('Digite o cateto oposto: '))
hy = hypot(ad,op)
print(f'A hipotenusa é {hy:.2f}')
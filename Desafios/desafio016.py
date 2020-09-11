# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a asua porção inteira
# EX: Digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6
from math import trunc
n = float(input('Digite um numero : '))
i = trunc(n)
print(f'O numero {n} tem a parte inteira {i}')

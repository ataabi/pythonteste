# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1,99),randint(1,99),randint(1,99),randint(1,99),randint(1,99))
print(f'{tupla}\nO maior número é ({tupla[-1]})\nE o menor é ({tupla[0]})')

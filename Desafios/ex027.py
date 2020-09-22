# Faça um programa que leia o nome completo de uma pessoa ,
# mostrando em seguida o primeiro e o ultimo nome peradamente.
# EX:Ana Maria de Sousa
# Primeiro = Ana
# ultimo = Souza
n = input('Digite seu nome Completo : ').strip()
split = n.title().split()
print(f'Primeiro nome : {split[0]}\n'
      f'Ultimo nome : {split[-1]}')
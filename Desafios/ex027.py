# Faça um programa que leia o nome completo de uma pessoa ,
# mostrando em seguida o primeiro e o ultimo nome peradamente.
# EX:Ana Maria de Sousa
# Primeiro = Ana
# ultimo = Souza
n = 'jhony patterson ribeiro faustino' #input('Digite seu nome Completo :\n')
split = n.title().split()
print(f'Primeiro nome : {split[0]}\n'
      f'Ultimo nome : {split[(len(split)-1)]:}')
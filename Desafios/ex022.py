# Crie um programa que leia o nome completo de uma pessoa e mostre :
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras tem ao T0do (sem considerar espaços)
# Quantas letras tem o primeiro nome

n = input('Digite seu nome: ')
print('-*-'*5)
split = n.split()
fn = len(split[0])
print(f'Seu nome em Maiusculo \n'
      f'{n.upper()},'
      f'\nSeu nome em Minusculo'
      f'\n{n.lower()}'
      f'\nSeu nome tem {(len(n))-(n.count(" "))} caracteres'
      f'\nE Somente seu primeiro nome tem {fn} caracteres ')
print('-*-'*5)

# Crie um programa que leia o nome completo de uma pessoa e mostre :
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras tem ao T0do (sem considerar espaços)
# Quantas letras tem o primeiro nome

n = input('Digite seu nome: ')
split = n.split()
print('\033[4:35m-*-\033[m'*18)
print(f'Seu nome em Maiusculo fica {n.upper()},'
      f'\nSeu nome em Minusculo fica {n.lower()}'
      f'\nSeu nome tem {(len(n))-(n.count(" "))} caracteres'
      f'\nE Somente seu primeiro nome tem {len(split[0])} caracteres ')
print('\033[4:35m-*-\033[m'*18)

# faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo.
print('Esse número é primo ?')
n = int(input('Digite um número: '))

if n%2 >= 1 and n%3 >= 1 and n%5 >= 1 and n%7 >= 1:
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')

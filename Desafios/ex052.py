# faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo.
print('Esse número é primo ?')
n = int(input('Digite um número: '))
#if n%2 >= 1 and n%3 >= 1 and n%5 >= 1 and n%7 >= 1:
#    print(f'{n} é um número primo')
#else:
#    print(f'{n} não é um número primo')
count = 0
for c in range(1,(n+1)):
    if n % c == 0 :
        print('\033[34m', end='')
        count += 1
    else:
        print('\033[31m',end='')
    print(f'{c} ',end='')
print(f'\n\033[mO número {n} foi divisível {count} vezes')
if count == 2:
    print('E por isso ele È PRIMO!')
else:
    print('E por isso ele NÃO E PRIMO!')
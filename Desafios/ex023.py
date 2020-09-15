#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#EX: Digite um numero: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1
n = int(input('Digite um numero entre 0 e 9999 \n: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número {n}. \n'
      f'{"*"*27}\n'
      f'Unidade : {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}')

print(f'{"-"*27}\n'
      f'|{"M":^5}|{"C":^5}|{"D":^5}|{"U":^5}|\n'
      f'{"-"*27}\n'
      f'|{m:^5}|{c:^5}|{d:^5}|{u:^5}|\n'
      f'{"-"*27}')

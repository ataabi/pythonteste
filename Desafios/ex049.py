#Refaça o desafio 009, mostrando a taboada de um numero que o usuario escolher, so que agora utilizando um laço for.
n = int(input('Digite um numero para ver sua taboada.\n: '))
print(f'Taboada do {n}\n','-'*11)
for c in range(1,11):
    print(f'{n:>2}x{c:>3} ={n*c:>3}')
print('-'*12)
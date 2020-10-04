# Faça um programa que leia 5 valores numéricos e guardeos em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas possições na lista
var = []
maior = 0
menor = 0
print('-='*22)
for c in range(0,5):
    n = int(input(f'Digite o Valor de posição {c}: '))
    var.append(n)
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('-='*22)
print(f'Os Valores digitados são {var}')
print(f'O menor valor é {menor} nas posições ',end=',')
for e, v in enumerate(var):
    if v == menor:
        print(f'[{e}]',end=' ')
print(f'\nO maior valor é {maior} nas posições ',end=',')
for e2, v2 in enumerate(var):
    if v2 == maior:
        print(f'[{(e2)}]',end=' ')
print('')
print('-='*22)

# faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.
print('Quem tem o Maior peso ?')
l = []
for c in range(0,5):
    p = float(input(f'({c+1}) - Qual seu peso ?: '))
    l.append(p)
l.sort()
print(f'O maior peso é {l[-1]} e o Menor é {l[0]}')
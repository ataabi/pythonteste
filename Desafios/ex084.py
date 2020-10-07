# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas forom cadastradas.
# B) uma listagem com as pessoas mais pesadas.
# C) uma listagem com as pessoas mais leves.
lista = ['Choco', 11.0, 'Billy', 24.0, 'Zeus', 25.0, 'Godi', 13.0]
menor = 0
maior = 0
while True:
    lista.append(str(input('Nome: ')).strip().title())
    lista.append(float(input('Peso: ')))
    esc = input('Deseja continuar[S/N]: ').strip().lower()
    if esc in 'n':
        break

print('-='*20)

for e,p in enumerate(lista[1::2]):
    if e == 0:
        menor = maior = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print(f'Foram Cadastradas {len(lista)/2:.0f} pessoas')
print(f'O maior peso é de ',end='')
for e,p in enumerate(lista):
    if p == maior:
        print(f'{lista[(e-1)]}, ',end='')
print(f'pesando {maior:.2f}Kg')

print(f'O menor peso de ',end='')
for e,p in enumerate(lista):
    if p == menor:
        print(f'{lista[(e-1)]}, ',end='')
print(f'pesando {menor:.2f}Kg')
print('-='*20)

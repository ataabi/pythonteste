# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas forom cadastradas.
# B) uma listagem com as pessoas mais pesadas.
# C) uma listagem com as pessoas mais leves.

lista = []
mainl = []
menor = maior = 0

while True:
    lista.append(str(input('Nome: ')).strip().title())
    lista.append(float(input('Peso: ')))
    if len(mainl) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    mainl.append(lista[:])
    lista.clear()
    esc = input('Deseja continuar[S/N]: ').strip().lower()
    if esc in 'n':
        break

print('-='*20)
print(f'Foram Cadastradas {len(mainl)} pessoas')

print(f'O menor peso é {menor}Kg de ',end='')
for c in mainl:
    if c[1] == menor:
        print(c[0],end='. ')
print()

print(f'O maior peso é {maior}Kg de ',end='')
for c in mainl:
    if c[1] == maior:
        print(c[0],end='. ')
print()

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.
lista = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {(c+1)}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append([n])
print(lista)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]}')
print(f'Os valores impares são {lista[1]}')


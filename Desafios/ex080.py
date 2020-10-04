# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista,
# já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela
var = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0:
        print(f'{n} foi adicionado na posição [0]')
        var.append(n)

    elif var[0] > n:
        print(f'{n} foi adicionado na posição [0]')
        var.insert(0,n)

    elif var[-1] < n:
        print(f'{n} foi adicionado na posição [{c}]')
        var.append(n)

    elif n > var[0] and n < var[1]:
        print(f'{n} foi adicianado na posição [1]')
        var.insert(1,n)

    elif n < var[-1] and n > var[-2]:
        print(f'{n} foi adicionado na posição [{c-1}]')
        var.insert(-1,n)

print(f'Os valores digitados forom {var}')

#Respota.
'''
lista = []
for c in range(0,5):
    n = int(input('Digiteum Valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Of valores digitados em ordem foram {lista}')
'''
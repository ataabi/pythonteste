# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas lista extras que vão contar apenas os valores pares e os valores impares digitados,
# respectivamente. Ao final, mostre o conteúdo das três lista geradas.
lista = []
lpar = []
limpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    esc = input('Deseja continuar [S/N] :? ').strip().lower()
    print('+-=-+' * 10)
    if esc in 'n':
        break

for c in lista:
    if c % 2 == 0:
        lpar.append(c)
    else:
        limpar.append(c)

print(f'Lista completa :\033[4:36m{lista}\033[m'
      f'\nLista com os números pares: \033[4:36m{lpar}\033[m'
      f'\nLista com os números impares: \033[4:36m{limpar}\033[m')
print('+-=-+'*10)
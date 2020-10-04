# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números forom digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    n = input('Digite um valor: ')
    if n.isnumeric() == True:
        n = int(n)
        valores.append(n)
    else:
        print('Valor Inválido.')

    esc = str(input('Deseja continuar [S/N]: ')).strip().lower()
    while not esc in 'sn':
        print('Comando Inválido')
        esc = str(input('Digite[S] para continuar ou [N] para finalizar.\n: ')).strip().lower()
    if esc == 'n':
        break

valores.sort(reverse=True)
print(f'Forom Digitados {len(valores)} números.'
      f'\nOs valores do maior para o menor é {valores}')

if 5 in valores:
    print(f'O Valor 5 se encontra na lista na posição {valores.index(5)}')
else:
    print('O valor 5 não se encontra na lista')
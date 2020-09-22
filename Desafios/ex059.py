#Crie um programa que leia dois valores e mostre um menu na tela.
#[1]Somar , [2]Multiplicar, [3]maior, [4]novos números, [5]sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input('Digite o 1° valor : '))
n2 = float(input('Digite o 2° valor : '))
while True:
    print('Qual operação deseja executar :')
    print('[1]Somar  [2]Multiplicar\n[3]maior  [4]novos números\n[5]sair do programa.')
    esc = int(input('Qual sua escolha ?\n: '))
    if esc == 1:
        print(f'A Soma de {n1} + {n2} = {n1+n2}')
    elif esc == 2:
        print(f'A multiplicação de {n1} x {n2} = {n1*n2}')
    elif esc == 3:
        if n1 > n2:
            print(f'O maor número é {n1}')
        else:
            print(f'O maor número é {n2}')
    elif esc == 4:
        n1 = float(input('Digite o 1° valor : '))
        n2 = float(input('Digite o 2° valor : '))
    else:
        break
print('Finalizando.')
sleep(1)
print('Finalizando..')
sleep(1)
print('Finalizando...')
sleep(1)
print('Programa Finalizado.')
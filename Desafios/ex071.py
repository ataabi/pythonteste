# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o
# valor a ser sacado(número inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues.
# OBS: considere que o caixa pussui cédulas de R$50, R$20, R$10 e R$1.
print('Bem Vindo ao \nCAIXA ELETRONICO VIRTUAL IMAGINARIO\nsaque o quanto quizer.')
print('Temos as cedulas imaginarias de \n(R$50  R$20  R$10  R$1.)')
n = int(input('Quanto irar Sacar ?'))
'''n50 = n // 50
n20 = (n%50)//20
n10 = (n%50)%20//10
n1 = ((n%50)%20)%10//1
print(f'R$50 ({n50})\n'
      f'R$20 ({n20})\n'
      f'R$10 ({n10})\n'
      f'R$1 ({n1})')'''
total = n
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
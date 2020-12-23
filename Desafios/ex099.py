# Faça um programa que tenha uma função chama maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles e o maior.
from time import sleep

def maior(*n):
    m = 0
    print("=*" * 28)
    print("Analizando os valores passados..."), sleep(0.7)
    for c in n:
        print(c,end=' '), sleep(0.5)
        if m < c:
            m = c
    print(f'. Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {m}')


maior(4,3,1,6,4,2,)
maior(3,4,6,9,5,2)
maior(3,4,2)
maior(0)
maior()
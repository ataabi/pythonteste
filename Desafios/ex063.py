# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma Sequencia de Fibonacci.
# ex 0>1>1>2>3>5>8
f = int(input('Digite um valor inteiro: '))
n = int(input('Quantos numeros deseja ver da sequencia ?'))
s = f
count = 0
while count != n:
    s = f + s
    if s == 0:
        s += 1
    print(s)
    f = f + s
    print(f)
    count += 1

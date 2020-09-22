# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.(Desconsiderando o flag)
s = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram Digitados {c} números e a soma de  todos eles é {s}')

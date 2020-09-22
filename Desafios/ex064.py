# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag)
s = c = 0
print('Calculadora infinita.\nPara finalizar Digite (999).')
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma de todos os valores é {s}\n'
      f'Com um total de {c} numeros digitados.')
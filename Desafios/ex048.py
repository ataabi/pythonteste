# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e
# que se encontram no intervalo de 1 até 500.
s = 0
for c in range(1,500):
    if c%3 == 0:
        s += c
print(f'A Soma de todos os valores multiplos de 3 entre 1 e 500 é iqual a \n: {s}')
# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e
# que se encontram no intervalo de 1 até 500.
s = 0
count = 0
for c in range(0,501,3):
    if c % 2 != 0:
        count += 1
        s += c
print(f'A Soma dos {count} valores impares multiplos de 3 entre 1 e 500 é iqual a {s}')
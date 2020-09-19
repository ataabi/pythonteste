#desenvolta um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for impar, desconsidere-0.
print('Calculo de numeros pares')
s = 0
for c in range(0,6):
    n = int(input('Digite um valor impar: '))
    if n%2 == 0:
        s += n
print(f'A soma dos numeros pares é {s}')
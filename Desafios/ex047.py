#Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.
print('Numeros Pares entre 1, 50')
for c in range(1,51):
    if c%2 == 0:
        print(c,end=",")
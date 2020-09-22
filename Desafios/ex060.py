#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120 . Teste usando While e depois  for
f = int(input('Digite um numero :'))
count = f
while count != 1:
    count += -1
    f = f*count
print(f)
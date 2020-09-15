#Faça um programa que leia tres numeros e mostre qual é o maior e qual e o menor
print('Digite 3 Valores')
n1 = float(input('1° numero : '))
n2 = float(input('2° numero : '))
n3 = float(input('3° numero : '))
deck = sorted([n1,n2,n3])
print(f'O maior é {deck[2]} e o menor é {deck[0]}')

#Faça um programa que leia tres numeros e mostre qual é o maior e qual e o menor
print('Digite 3 Números')
n1 = float(input('1° numero : '))
n2 = float(input('2° numero : '))
n3 = float(input('3° numero : '))
if n3 < n2 < n1:
    print(f'O Maior N° é {n3} e o menor é {n1}')
elif n2 < n3 < n1:
    print(f'O Maior N° é {n1} e o menor é {n2}')
elif n3 < n1 < n2:
    print(f'O Maior N° é {n2} e o menor é {n3}')

#deck = sorted([n1,n2,n3])
#print(f'O maior é {deck[2]:.2f} e o menor é {deck[0]:.2f}')
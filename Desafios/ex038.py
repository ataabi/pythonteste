# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior.
# o segundo valor é maior.
# não existe valor maior, os dois são iguais.
print('Digite 2 valores abaixo.')
n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))
if n1 > n2:
    print('O primeiro número é maior')
elif n1 < n2:
    print('O segundo número é maior')
else:
    print('Os números são iquais.')

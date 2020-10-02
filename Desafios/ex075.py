# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
# A) quantas vezes apareceus o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
nums = (int(input('Digite o primeiro Valor: ')),
        int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')),
        int(input('digite o quarto valor: ')))
print(nums)
print(f'O número 9 aparece {nums.count(9)}')
print(f'O primeiro 3 aparece na posição {nums.index(3)}')
#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a R$1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual o salario do funcionario ? \n:'))
if s <= 1250.00:
    print(f'Com um aumento de 15%, o novo salario será de {(s+(s*0.15)):.2f}')
else:
    print(f'Com um aumento de 10%, o novo salario será de {(s+(s*0.10)):.2f}')
# Crie um programa que leia o ano de nascimento de sete pessoas.
# no final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja são maiores
from datetime import date
ano = date.today().year
print('Você ja é maior de idade ?')
maior = 0
menor = 0
for c in range(0,7):
    nas = int(input('Em que ano vc nasceu ?'))
    if ano-nas < 18:
        menor += 1
    elif ano-nas >= 18:
        maior += 1
print(f'Maior:{maior}, Menor: {menor}')
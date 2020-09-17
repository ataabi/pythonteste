# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# até 9 anos : Mirim
# ate 14 anos : infantil
# até 19 anos: junior
# até 20 anos: senior
# acimas: Master

from datetime import date
data = date.today().year
burn = int(input('Em que ano o Atleta nasceu ?\n: '))
print(f'Categoria: ', end='')
if data-burn <= 9:
    print('Mirim')
elif data-burn <= 14:
    print('Infantil')
elif data-burn <= 19:
    print('Junior')
elif data-burn <= 20:
    print('Senior')
else:
    print('Master')
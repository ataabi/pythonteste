# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar.
# se é a hora de se alistar.
# se já passou do tempo do alistamento.
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo;
from datetime import date
dia = date.today()
ano = int(input('Em que ano você nasceu ? \n: '))
age = (dia.year)-ano
print(f'{((dia.year)-ano)}')
if age <= 17:
    print(f'Você ainda vai se elistar espere so mais {18-age} anos para isso')
elif age == 18:
    print(f'Se deu mal ta na hora de se alistar.')
elif age >= 19:
    print(f'Sorte a sua ja passou {age-18} anos deis de seu alistamento')
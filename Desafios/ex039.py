# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar.
# se é a hora de se alistar.
# se já passou do tempo do alistamento.
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo;
from datetime import date
dia = date.today().year #Ano Atual
ano = int(input('Em que ano você nasceu ? \n: ')) #Data de nascimento do Cantidato
age = (dia)-ano # Idade do Canditado
print(f'Em {dia} você tem {age}')
if age <= 17:
    print(f'Seu alistamento sera em {ano+18} ainda faltam {18-age} anos para isso')
elif age == 18:
    print(f'Se deu mal ta na hora de se alistar.')
elif age >= 19:
    print(f'Sorte a sua ja passou {age-18} anos des de seu alistamento')

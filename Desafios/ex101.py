# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÒRIO
# nas eleições.

def voto(ano):
    from datetime import date
    i = 2018-ano #date.today().year - ano
    return  i


i = voto(int(input('Em que ano você nasceu ? ')))

if i <= 15:
    print(f'Com {i} anos, o você não pode votar.')
elif i <=17:
    print(f'Com {i} anos, o voto é opcional')
elif i <=64:
    print(f'Com {i} anos, o voto é obrigatório')
else:
    print(f'Com {i} anos, o voto é opcional')



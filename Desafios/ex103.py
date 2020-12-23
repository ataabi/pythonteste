# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome="<desconhecido>", gols=0):
    """
    -> Mostra as dados de um Jogador.
    :param nome: Nome do jogador
    :param gols: quantidade de gols feito.
    :return: No Return
    """
    print(f'O jogador {nome} fez {gols} no campeonato.')


n = input('Nome do jogador: ').strip()
g = input('Número de Gols: ').strip()
if g.isnumeric() == True:
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)

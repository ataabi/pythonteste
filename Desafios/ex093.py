# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada cada partida. no final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
apro = {}
gols = []
apro['jogador'] = str(input('Qual o nome do jogador: ')).title()
apro['partidas'] = int(input(f'Quantas partidas {apro["jogador"]} jogou ? '))
for p in range(0,apro['partidas']):
    gols.append(int(input(f'Quantos gols {apro["jogador"]} vez no {p+1}ª jogo ? ')))
apro['gols'] = gols[:]
apro['total'] = sum(gols)
print('=o'*40)
print(apro)
for k,v in apro.items():
    print(f'O campo {k} tem o valor {v}')
print('=o'*40)
print(f'{apro["jogador"]} jogou {apro["partidas"]} partidas.')
for e,v in enumerate(apro["gols"]):
    print(f'  => Na {e+1}º partida marcou {v} gols.')
print(f'Com um total de {apro["total"]} de gols.')
print('=o'*40)



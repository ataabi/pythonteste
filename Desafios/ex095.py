# aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.
'''
gols = []
geral = []
jogador = {}
tot = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    print(f'Quantos gols {jogador["nome"]} marcou na.')
    for p in range(0,jogador['partidas']):
        gols.append(int(input(f'{p+1}º partida: ')))
        tot += gols[p]
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    geral.append(jogador.copy())
    gols.clear()
    tot = 0
    print('-' * 40)
    esc = str(input('Continuar ? [S/N]: ')).strip().lower()
    if esc in 'n':
        break

print('-'*40)
print(f'|{"cod":^3}|{"Nome":^12}|{"Gols":^15}|{"Total":<5}|')
print('-'*40)
for e, c in enumerate(geral):
    print(f'|{e:^3}| {c["nome"]:<11}| {" ".join(map(str,c["gols"])):<14}|{c["total"]:^5}|')
print('-'*40)


print('-'*40)

while True:
    esc = int(input('Analize detalhada [Digite 999 para sair]\n'
                    ' Deseja ver qual jogador ? cod: '))
    while esc >= int(len(geral)) and esc < 998:
        print('ERRO! Esse jogador não existe')
        esc = int(input('Mostrar dados de qual jogador ? '))
        print('-' * 40)
    if esc == 999:
        break
    for k,v in geral[esc].items():
        if k == "nome":
            print(f' O jogador {v} jogou',end=' ')
        if k == 'partidas':
            print(f'{v} partidas')
        if k == "gols":
            for e,g in enumerate(v):
                print(f'  - No {e+1}º jogo marcou {g} gols ')
        if k == "total":
            print(f' Total de gols : {v}')
print(f' {"-- FIM - -":^40}')
'''
# Respota

time = []
partidas = []
jogador = {}

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
    jogador.clear()

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-='* 40)
for k , v in enumerate(time):
    print(f'{k:^3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o cod:{busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez  {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')



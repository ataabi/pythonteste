# Crie um tupla preenchida com os 20 primeiros colocados da tabela do compeanato brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) os Ultimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tavela está o time da Chapecoense.
from random import randint
tabela = ('Atlético-MG','Internacional','São Paulo','Palmeiras','Vasco','Flamengo','Fluminense','Sport','Santos',
          'Fortaleza','Athletico-PR','Ceará','Atlético-GO','Grêmio','Corinthians','Coritiba','Bragantino',
          'Botafogo','Goiás','Bahia')
print('º'*40,
    '\nOs 5 Primeiros Colocado são.\n',
    tabela[:5])
print('º'*40,
    '\nOs 4 ultimos colocados são.\n',
    tabela[16:])
print('º'*40,
      '\nTodos os Times em ordem alfabética.\n'
   f'{sorted(tabela)}')
print('º'*40)
r = randint(1,20)
print(f'O Time {tabela[r]} esta na {(r+1)}ª posição')
print(f'O Time {tabela[tabela.index("Santos")]} esta na {(tabela.index("Santos")+1)}ª posição')
#Chapecoence nao ta na tabela. Vou usar O Santos.
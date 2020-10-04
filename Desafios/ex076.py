# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, Mostre uma listagem de preços, organizando os dados em forma tabular
prod = ('banana',2.40,'maça',4.90,'batata',2.50,'miojo',1.20,'bolacha',0.90,'sabão',1,'arroz',11.20,'feijão',7.30,
        'sorvete',16.90,'açucar',2.05,'oleo',6.50)

print('*'*34)
print(f'{" Lista de Produtos ":*^34}')
print('*'*34)

for e ,p in enumerate(prod):

    if e % 2 == 0:
        print(f'* {p:-<20}', end='')

    if e % 2 != 0:
        print(f'R$ {p:>7.2f} *')

print('*'*34)

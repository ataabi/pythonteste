# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, Mostre uma listagem de preços, organizando os dados em forma tabular
prod = ('banana',2.40,'maça',4.90,'batata',2.50,'miojo',1.20,'bolacha',0.90,'sabão',1,'arroz',11.20,'feijão',7.30)
produtos = []
valor = []
count1 = 1
count2 = 0
print('*'*27)
print(f'{" Lista de Produtos ":*^27}')
print('*'*27)
for c in prod:
    count1 += 1
    count2 += 1
    if count1%2 == 0 :
        print(f'* {c:-<20}', end='')
    if count2%2 == 0 :
        print(f'{c:2.2f}*')
print('*'*27)

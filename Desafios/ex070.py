#Crie um programa que leia o nome e preço de varios produtos. O programa deverá perguntar se o usuário vai continuar.
# no final, mostre:
# A-) qual é o total gasto na compra.
# B-) Quantos produtos custam mais de R$1000.
# C-) Qual é o nome do produto mais barato.
dic = {}
s = 0 #Soma dos produtos
cp = 0 #Contador de produtos acima de 1000
while True:
    np = str(input('Nome do Produto: ')).strip().title() #nome do prodruto
    pp = float(input('Preço do Produto: ')) #Preço do produto
    if pp > 1000:
        cp += 1
    dic[pp] = np
    s += pp
    esc = input('Continuar (S/N) :').strip().lower()
    if 'n' in esc:
        break

v = sorted(dic.keys()) #Levando as os precos para uma lista
print(f'Produto mais barato é {dic[v[0]]}')
print(f'Soma dos produtos {s}')
print(f'Produtos que custom mais de 1000 : {cp}')
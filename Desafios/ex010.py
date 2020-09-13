# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considere us1,00 = r$3,27.
rs = float(input('Quanto dinheiro você tem na carteira ? \nR$'))
d = 3.27
print(f'Você tem R${rs} com o dolar a ${d} voce pode comprar US${(rs/d):.2f}')
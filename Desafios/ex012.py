# Faça um programa que leia o preco de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Digite o valor do produto : R$'))
d = p*0.05
print(f'O produto custa R${p} e com 5% de desconto, '
      f'\nvocê tera R${d:.2f} e vai te custa R${(p-d):.2f}.')


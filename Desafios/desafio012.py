# Faça um programa que leia o preco de um produto e mostre seu novo preço com 5% de desconto.
p = int(input('Digite o valor do produto : '))
d = p
print(f'O produto custa R${p} e com 5% de desconto, '
      f'\nvocê tera R${d} e vai te custa R${(p-d)}.')
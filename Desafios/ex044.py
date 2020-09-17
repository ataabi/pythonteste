# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# á vista dinheiro/cheque: 10% de desconto
# á vista no cartão: 5% de desconto
# em até 2x no cartão: preoço normal
# 3x ou mais no cartão: 20% de juros
print('Calculo do valor com parcelamento, juros e desconto.')
produto = float(input('Qual o valor do produto :'))
print('Digite : (1)\nPagamento á vista Dinheiro/Cheque:(10% de desconto)\n'
      'Digite : (2)\nPagamento á vista no cartão:(5% de desconto)\n'
      'Digite : (3)\nPagamento em até 2x no cartão:(Sem juros)\n'
      'Digite : (4)\nPagamento em 3x ou mais no cartão:(20% de juros)')
var = int(input(': '))
if var == 1:
    print(f'Sairá por R${produto-(produto*0.10)}.')
elif var == 2:
    print(f'Sairá por R${produto-(produto*0.05)}')
elif var == 3:
    print(f'Sairá por 2x R${produto/2}')
else:
    vezes = int(input('Em quantas vezes ?'))
    print(f'Sairá por {vezes}x R${((produto+(produto*0.20))/vezes)}, total de R${produto+(produto*0.20)}')
print('Boas Compras.')
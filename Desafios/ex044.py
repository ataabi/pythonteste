# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# á vista dinheiro/cheque: 10% de desconto
# á vista no cartão: 5% de desconto
# em até 2x no cartão: preoço normal
# 3x ou mais no cartão: 20% de juros
print('Calculo do valor com parcelamento, juros e desconto.')
produto = float(input('Valor Total : R$'))

print('FORMAS DE PAGAMENTO:\n'
      '(1) Pagamento á vista Dinheiro/Cheque:(10% de desconto)\n'
      '(2) Pagamento á vista no cartão:(5% de desconto)\n'
      '(3) Pagamento em até 2x no cartão:(Sem juros)\n'
      '(4) Pagamento em 3x ou mais no cartão:(20% de juros)')
var = int(input(': '))
if var == 1:
    print(f'Sairá por R${produto-(produto*0.10):.2f}.')
elif var == 2:
    print(f'Sairá por R${produto-(produto*0.05):.2f}')
elif var == 3:
    print(f'Sairá por 2x R${produto/2:.2f}')
elif var == 4:
    vezes = int(input('Em quantas vezes ?'))
    print(f'Sairá por {vezes}x R${((produto+(produto*0.20))/vezes):.2f}, total de R${produto+(produto*0.20):.2f}')
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')
print('Boas Compras.')

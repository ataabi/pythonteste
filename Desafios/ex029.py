#EScreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.
v = float(input('Em que velocidade estava o carro ?'))
m = (v-80)*7
if v >= 80:
    print('Voce ultrapassou os limites de velocidade.\n'
          f'você tera que pagar uma multa de R${m}')
else:
    print('Continue a dirigir com segurança.')
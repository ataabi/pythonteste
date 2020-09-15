#Desenvola um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preoço da passagem, cobrando R$0,05 por Km para viagens até 200km
#e R$0.45 para viagens mais longas.
v = float(input('Quantos KM você vai viagar ?'))
if v <= 200:
    print(f'{v*0.50}')
else:
    print(f'{v*0.45}')
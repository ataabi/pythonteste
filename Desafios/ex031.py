#Desenvola um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preoço da passagem, cobrando R$0,05 por Km para viagens até 200km
#e R$0.45 para viagens mais longas.
km = float(input('Quantos KM você vai viagar ? '))
v = km*0.50 if km <= 200 else km*0.45 # IF simplificado
print(f'A passagem vai te custar R${v:.2f}')
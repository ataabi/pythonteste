# desenvola uma logica que leia o peso e a altua de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabelta abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40 : Obesidade
# Acima de 40: Obsidade mórbida
print('Cálculo do IMC')
alt = float(input('Qual sua Altura ?\n: '))
pes = float(input('Qual seu peso ?\n: '))
imc = pes/alt**2
print(f'\nSeu IMC: {imc:.2f} : ',end ='')
if imc < 18.5:
    print('Squeleto')
elif imc < 25:
    print('Fitness')
elif imc < 30:
    print('Gordin')
elif imc < 40:
    print('Gordão')
elif imc > 40:
    print('JAMANTA')
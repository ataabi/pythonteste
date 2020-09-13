# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
m = float(input('Digite um valor em metros: '))
cm = m*100
mm = m*1000
print(f'{m}m é equivalente a\n'
      f'{m/1000}km \n'
      f'{m/100}hm \n'
      f'{m/10}dam \n'
      f'{m*10:.0f}dm \n'
      f'{cm:.0f}cm \n'
      f'{mm:.0f}mm')
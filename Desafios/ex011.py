# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua area e a quantidade de tinta nescessaria para pinta-la,
# sabendo que cada litro de tinta pinta uma area de 2m²

print('Digite a altura e a largura da parede a ser pintada'
      '\npara calcular a área e saber quanto de tinta você irar precissar')
a = float(input('Digite a Altura :'))
l = float(input('Digite a Largura : '))
area = a*l
print(f'Essa paredere possui {a}m x {l}m com uma área de {area:.2f}m²\n'
      f'Você ira precissar de {(area/2):.2f}l de tinta para pintar a parede ')

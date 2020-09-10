# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua area e a quantidade de tinta nescessaria para pinta-la,
# sabendo que cada litro de tinta pinta uma area de 2m²

print('Digite a altura e a largura da parede a ser pintada'
      '\n para calcular a area e saber quanto de tinta você irar precissar')
a = int(input('Digite a Altura :'))
l = int(input('Digite a Largura : '))
area = a*l
print(f'Você ira precissar de {(area/2)}l de tinta para pintar a parede ')

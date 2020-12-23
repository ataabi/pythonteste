# faça um programa que tenha uma função chama aréa(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(l,c):
    r = l*c
    print(f'A aréa do de um terreno com {c}m comprimento e {l}m largura  é {r}m²')

# MainBody
print(' Controle de Terreno')
print('-'*21)
l = float(input('Largura (m): '))
c = float(input("Comprimento (m): "))
area(l,c)
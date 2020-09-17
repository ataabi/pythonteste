# Refaça o desafio 035 dos triangulos, acrescentando  o recuso de mostrar que tipo de triangulo sera formado:
#equilatero: todos os lados iguais
# isósceles : dois lados iguais
# Escaleno : todos os lados diferentes
print('Vamos ver se essas retas fomam um triangulo ?')
r1 = int(input('1° Reta :'))
r2 = int(input('2° Reta :'))
r3 = int(input('3° Reta :'))
if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('Essas retas fomam um Triangulo.')
    if r1 == r2 == r3:
        print('Esse é um Triangulo Equilatero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esse é um Triangulo Isósceles.')
    else:
        print('Esse é um Triangulo Escaleno.')
else:
    print('Essas Retas nao fomam um Triangulo')
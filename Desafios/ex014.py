# Escreva um programa que converta uma temperatura de C° para F°
c = float(input('Digite a temperatura em C°: '))
f = c*9/5+32
ct = (f-32)*5/9
print(f'A temperatura de {c}C° corresponde a {f:.1f}F°')
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0.15 por Km rodado.
d = int(input('Quantos dias você ficou com o carro ? '))
km = float(input('Quantos Km você andou ? '))
a = (d*60)+(km*0.15)
print(f'O aluguel vai ficar em R${a:.2f}.')
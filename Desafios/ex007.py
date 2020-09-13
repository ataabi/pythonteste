# Desemvola um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
a = input('Qual o nome do aluno ? ')
print('Digite as Notas do aluno')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print(f'A Média entre {n1:.1f} e {n2:.1f} do aluno {a} é igual {m:.1f}')
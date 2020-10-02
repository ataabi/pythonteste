# crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final
# de acordo com o media atiginda:
# média abaixo de 5.0: reprovado
# média entre 5.0 e 6.9: Recuperação
# média 7.0 ou superior: aprovado
# nome = input('Nome do aluno: ')
print('Quais forom as notas do aluno ?')
n1 = float(input(f'Qual a 1°: '))
n2 = float(input(f'Qual a 2°: '))
m = (n1+n2)/2
print('-'*40)
print(f'''|{'Nota 1':^8}|{'Nota 2':^8}|{'Média':^7}|{'Status':^8}|''')
print('-'*40)
if m < 5.0:
    print((f'''|{n1:^8}|{n2:^8}|{m:^7}|\033[31m{'Reprovado':^8}\033[m|'''))
elif m < 6.9:
    print((f'''|{n1:^8}|{n2:^8}|{m:.2f^7}|\033[33m{'Recuperação':^8}\033[m|'''))
else:
    print((f'''|{n1:^8}|{n2:^8}|{m:^7}|\033[32m{'Aprovado':^8}\033[m|'''))
print('-'*40)
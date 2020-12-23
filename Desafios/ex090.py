# Faça um programa que leia nome e média de um aluno, guardando tambem a situação em um dicionário.
# No final mostre o canteúdo da estruta na tela.

dic = {}
dic['nome'] = str(input('Nome do aluno: '))
dic['media'] = float(input(f'Média de {dic["nome"]}: '))

if dic['media'] >= 7:
    dic['situação'] = 'Aprovado'
elif dic['media'] <= 5:
    dic['situação'] = 'Reprovado'
elif dic['media'] < 7:
    dic['situação'] = 'Recuperação'

print('-=' * 30)
print(f'A média de {dic["nome"]} é {dic["media"]} que esta {dic["situação"]}')
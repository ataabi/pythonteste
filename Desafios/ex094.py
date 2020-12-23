# Crie um programa que leia nome,sexo e idade de varioas pessoas, guardando os dados de cada pessoa em um dicionario e
# todos os dicionarios em uma lista. no final, mostre:
# A Quantas pessoas foram cadastradas
# B A média de idade do grupo
# C uma lista com todas as mulheres.
# D Uma lista com todas as pessoas com idade acima da média.

geral = []
pessoas = {}
somaidade = 0

while True:
    pessoas["nome"] = str(input('Nome: ')).strip().title()

    sexo = str(input('Sexo [M/F]: ')).strip().title()
    while sexo not in 'FM':
        print('ERRP! Por favor, digite apenas M ou F')
        sexo = str(input('Sexo [M/F]: ')).strip().title()
    pessoas['sexo'] = sexo

    idade = input('Idade: ')
    while True:
        if idade.isnumeric() == True:
            idade = int(idade)
            break
        else:
            print('ERRO! Valor inválido com idade. Digite apenas números')
            idade = input('Idade: ')
    pessoas['idade'] = idade

    somaidade += pessoas['idade']
    geral.append(pessoas.copy())

    while True:
        esc = str(input('Deseja continuar ? [S/N]: ')).strip().lower()
        if esc in 'sn':
            break
        else:
            print('ERRO! Digite apenas S ou N')
    if esc == 'n':
        break

print("-*"*40)
print(f'- O número de cadastro é {len(geral)}\n'
      f'- A média de idade é {somaidade/len(geral):.2f}')

print('- As mulhers são ',end='')
for c in geral:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}',end='. ')
print('')

print('- As pessoas com a idade acima da média são:')
for c in geral:
    if c['idade'] >= (somaidade/len(geral)):
        print(f' --* {c["nome"]} com {c["idade"]} anos do sexo',end=' ')
        if c["sexo"] in "M":
            print('Masculino')
        else:
            print('Feminino')
print()
print("-*"*40)

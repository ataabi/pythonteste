# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre?
# A-) Quantas pesoas tem mais de 18 anos.
# B-) Quantos homens foram cadastrados.
# C-) Quantas mulheres tem menos de 20 anos.
coid = 0 # Contador de pessoas maiores de 18
cose = 0 # Contado de Sexo Masculino
co20 = 0 # Contador de mulheres menores de 20
print('=-*-='*10)
print('CADASTRO DE PESSOAS')
print('=-*-='*10)
while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        coid += 1
    sexo = str(input('(H)-Homen, (M)-Mulher\nDigite seu sexo: ')).strip().lower()
    if 'h' in sexo:
        cose += 1
    if idade < 20 and 'm' in sexo:
        co20 += 1
    esc = str(input('Deseja Continuar (S/N)?: ')).strip().lower()
    print('=-*-=' * 10)
    if 'n' in esc:
        break
print(f'Foram cadastradas {coid} pessoas maiores de 18 anos.')
print(f'{cose} Homens e {co20} mulheres menores de 20')

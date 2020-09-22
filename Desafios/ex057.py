#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou 'F', caso esteja errado, pega a digitação novamente até ter um valor correto.
while True:
    ge = str(input('''(M) para Masculino. (F) para Feminino : ''')).upper()
    if ge == 'M':
        print('Você é um Homen')
        break
    elif ge == 'F':
        print('Você é uma Mulher')
        break
    elif ge != 'F' or ge != 'M':
        print('Comando não reconhecido\n    Digite F ou M.')
print('È isso ai.')
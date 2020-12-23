# Crie um programa que leia nome, ano de nascimento e cateira de trabalho e cadaste-os(com idade) em um dicionario
# se por acaso a CTPS for diferente de zero, o dicionário receberá tambem o ano de contratação e o salário.
# Calcule e acrescente, alem da idadem com quantos anos a pessoa vai se aposentar.
from datetime import date
dic = {}
dic["nome"] = str(input('Digite seu nome: '))
nasc = int(input(f'Em que ano você nasceu {dic["nome"]}: '))
dic['idade'] = date.today().year - nasc
dic['ctps'] = int(input('Sua carteira de trabalho (0 se nao tiver): '))

if not dic["ctps"] == 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário : R$ '))
    dic['Aposentadoria'] = (dic['contratação']-nasc)+35

print('='*30)
for k,v in dic.items():
    print(f'- {k.title()} tem o valor {v}')
print('='*30)



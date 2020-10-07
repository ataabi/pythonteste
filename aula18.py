galera = []
dado = []
maior = menor = 0
print('-=' * 20)
for c in range(0,3):
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(int(input('Idade: ')))
    print('-='*20)
    galera.append(dado.copy())
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1

print(f'Temos {maior} maiores e {menor} menores de idade')


'''
galera = [['João',10],['Ana',33],['Joaquim',13],['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

teste = []
teste.append('billy')
teste.append(4)
galera = []
galera.append(teste[:])
teste[0] = 'Choco'
teste[1] = 3
galera.append(teste[:])
print(galera)
'''
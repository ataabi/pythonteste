# desenvola um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# a media de idade do grupo
# qual é o nome do homen mais velho.
# quantas mulheres tem menos de 20 anos.
l = {}
lm = []
m = 0 # contador de media
cm = 0 # Contador de mulheres
for c in range(0,4):
    print(f'---------- {c+1}° PESSOA ----------')
    nome = input('Nome : ').title()
    idade = int(input('Idade : '))
    m += idade
    sexo = input('Sexo (M/F): ').title()
    if 'F' in sexo:
        if idade < 20:
            cm += 1
    elif 'M' in sexo:
        l[idade] = nome
        lm.append(idade)
sorted(lm)
older = int(lm[-1])
print(f'A Média de idade é >{m/4}<,')
print(f'O Homen mais velho é > {l[older]} <')
print(f'E o número de mulheres menores de 20 é >{cm}<')

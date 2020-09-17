nome = str(input('Qual é seu nome?\n: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssiaca Juliana':
    print('Belo nome feminino')
elif nome.title() in ('Billy Choco Zeus Godi'):
    print('Que nome do caralho. \033[7mSHOW DE BOLA\033[m')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um dom dia, \033[31m{nome}\033[m!')
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('miojo','biscoito','cachorro','monitor','cocacola','agua')
vogais = ('a','e','i','o','u')
count = 0
for p in palavras:   # Separando a tupla em strings
    print(f'\nA Palavra \033[33m{p.upper()}\033[m tem as seguintes vogais',end=' = ')
    for l in p:   # Separando as Strings em letras
        if l in vogais:  # Verificando as Vogais
            print(f'[\033[31m{l}\033[m]',end='')

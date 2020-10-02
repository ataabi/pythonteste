# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
vogais = ('a','e','i','o','u')
palavras = ('miojo','biscoito','cachorro','monitor','cocacola','agua')
count = 0
for p in palavras:   # Separando a tupla em strings
    print(f'\nA Palavra {p} tem as seguintes vogais',end=' = ')
    for l in p:   # Separando as Strings em letras
        if l in vogais:  # Verificando as Vogais
            print(f'[{l}]',end='')

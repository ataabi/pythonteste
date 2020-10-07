# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#    [][][]         No final, mostre a matriz na tela, com a formatação correta.
#    [][][]
#    [][][]
'''
matriz = [[],[],[]]
for c in range(0,9):
    if c <= 2:
        n = int(input(f'Digite o valor da posição (0,{c}): '))
        matriz[0].append(n)
    elif c <= 5:
        n = int(input(f'Digite o valor da posição (1,{(c-3)}): '))
        matriz[1].append(n)
    elif c <= 9:
        n = int(input(f'Digite o valor da posição (2,{(c-6)}): '))
        matriz[2].append(n)
print('-='*20)

for c in matriz[0]:
    print(f'[ {c} ]',end='')
print()
for c in matriz[1]:
    print(f'[ {c} ]', end='')
print()
for c in matriz[2]:
    print(f'[ {c} ]', end='')
'''

# Resposta.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posição ({l},{c}): '))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
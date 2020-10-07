# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = 0
colun3 = 0
# Contrução da Matriz
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posição ({l},{c}): '))
print('-='*25)
# Exibição da Matriz
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    if matriz[l][2] != 0:
            colun3 += matriz[l][2]
    print()
# Analize dos dados na matriz
print('-='*25)
print(f'A soma de todos os valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {colun3}')
matriz[1].sort()
print(f'E maior valor da segunda linha é {matriz[1][-1]}')
print('-='*25)
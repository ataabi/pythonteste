# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro,ele não será adicionado. No final seão exibido todos os valors
# únicos digitados, em ondem crescente.
var = []
while True:
    n = int(input('Digite um valor: '))
    if n not in var:
        print(f'O Valor {n} foi adionado com sucesso.')
        var.append(n)
    else:
        print('Esse valor ja se encontra na lista.')
    esc = input('Deseja continuar[S/N]?: ').strip().lower()
    while not esc in 'sn':
        esc = input('Valor inválido, Deseja continuar[S/N]?: ').strip().lower()
    if esc == 'n':
        break
print('#='*20)
var.sort()
print(f'Os valores únicos digitados forom {var}')

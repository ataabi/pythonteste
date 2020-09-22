#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O progroma sera interrompido quando o número solicitado for negado.
print('TABUADA')
print('para finalizar entre com um valor negativo.')
while True:
    n = int(input('Digite um valor: '))
    print('='*20)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{c:>2} X {n} = {c*n}')
    print('=' * 20)
print('FIM')
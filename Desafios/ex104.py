# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante função input() do python
# só que fazendo a validção para aceitar apenas um valor numérico.
#ex: n = leiaint('Digite um número')

def leiaint(n='Digite um valor inteiro: '):
    while True:
        num = str(input(f'{n}'))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f'\033[31mERRO! Essa valor não é um número.\033[m')



n = leiaint(':>')
print(f'Você digitou o número {n}')

z = leiaint('teste fase:> ')
print(z)
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome idade em um arquivo de texto simples
# O sistema só vai ter 2 opcôes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def registro(nome, idade):
    '''
    Cria um arquivo para armazenamento de nome e idade
    :param nome: Nome a ser Cadastrado
    :param idade: Idade a ser Cadastrada
    :return:
    '''
    with open('banco.txt', 'a') as texte:
        print(f'{nome:<40}|{idade:^5}', file=texte)


def checknum(msg):
    while True:
        num = input(msg)
        try:
            num = int(num)
        except:
            print('Por Favor digite um valor inteiro.')
        else:
            return num

# Main program
while True:
    print('-' * 46)
    print(f'{"Gerenciador de Usuários":^46}')
    print('-' * 46)
    print('(1) Cadastro de pessoas \n(2) Lista de Cadastros \n(3) Finalizar')
    esc = checknum(': ')

    try:
        if esc == 1:
            nome = input('Nome: ').title()
            idade = checknum('Idade: ')
            registro(nome, idade)

        elif esc == 2:
            print(f'{"Nome":<40}|{"Idade":^5}')
            print('-' * 46)
            for t in open('banco.txt'):
                print(t.title().strip())

        elif esc == 3:
            break

        else:
            print('\033[31mOpção inválida.\033[m')

    except:
        print('')

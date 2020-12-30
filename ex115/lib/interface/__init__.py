def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro: Este valor não é um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt) :
            print('\033[31mNenhum Valor Digitado.\033[m')
            return 0
        else :
            return n


def linha(tam = 45):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())


def menu(lista):
    cabeçalho('MENU')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaint(':> ')
    return opc

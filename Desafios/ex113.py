# Reescreva o função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesmo funcionalidade.

def leiaInt(msg):
    """
    :param msg: Analiza se o valor é inteiro
    :return: O valor inteiro
    """
    while True:
        try:
           i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro: Este valor não é um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mNenhum Valor Digitado.\033[m')
            return 0
        else:
            return i

def leiaFloat(msg=': '):
    """
    :param msg: Analiza se o valor évalor Real
    :return: O valor Real
    """
    while True:
        try:
            f = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mNenhum Valor Digitado.\033[m')
            return 0
        except:
            print('\033[31mErro. Por favor digite um valor real válido.\033[m')
            continue
        else:
            return f

#Main Body
ni = leiaInt('Digite um valor inteiro:> ')
nr = leiaFloat('Digite um valor real:> ')
print(f'O número inteiro foi {ni} e o numero Real foi {nr}')

# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a paravra 'FIM', o programa se encerrará. OSB: USE CORES.

def ajuda():
    from time import sleep
    print('\033[7:30m-*'*13)
    print('|Sistema de Ajuda PyHelp |')
    print('-*'*13,'\n\033[m',end='')
    ajuda = str(input('Função da Biblioteca :> '))
    while ajuda not in 'FIM':
        v = int(len(ajuda))
        print('\033[7:34m-*' * (17+v))
        print(f'  Procurando por [{ajuda}] na Biblioteca ...')
        print('-*' * (18+v),'\n\033[m',end='')
        sleep(1)
        print('\033[7:32m')
        help(ajuda)
        print('\033[m')
        ajuda = str(input('Função da Biblioteca :> '))


ajuda()
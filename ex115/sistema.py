from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resp = menu(['Ver Cadastros', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        #opção de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:> '))
        idade = leiaint('Idade:> ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO. Digite uma opção valida\033[m')
    sleep(1)


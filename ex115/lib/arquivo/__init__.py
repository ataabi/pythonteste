from  ex115.lib.interface import *

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Não foi possivel criar o arquivo {nome}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt' )
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.strip().split(';')
            print(f'{dado[0]:<35}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRo na hora de escrever os dados')
        else:
            print(f'{nome} adicionado com sucesso ao registro.')
            a.close()


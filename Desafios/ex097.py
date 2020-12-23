# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.
#Ex
#escreva('Ola,Mundo!')
#Saida
#------------
# Ola,Mundo!
#------------
def escreva(txt):
    v = int(len(txt))+2
    print('~'*v)
    print(f' {txt} ')
    print('~'*v)


while True:
    txt = input(">")
    escreva(txt)
    if txt in 'sair':
        break
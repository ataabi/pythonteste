#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaçõs.
#ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO , ANOTARAM A DATA DA MARATONA
import unicodedata
print('*'*45,'\nVamos ver se essa frase é um palindromo.')
f = input('Digite uma Frase. \n: ')
f = unicodedata.normalize('NFD',f)
print(f'A Frase: {f.title()}')
f = f.encode("ascii", "ignore")
f = f.decode("utf-8")
f = f.replace(' ','')
r = f.replace(' ','')[::-1]
if f == r:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
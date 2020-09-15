#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo".
n = input('Digite o nome da Cidade \n:')
if n.find("Santo") == 0:
    print('O nome da sua cidade se inicia com Santo')
else:
    print('O nome da sua cidade nao se inicia com Santo')
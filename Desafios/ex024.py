#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo".
n = str(input('Digite o nome da Cidade \n:')).strip
s = n.title().split()
print(s[0] == 'Santo')
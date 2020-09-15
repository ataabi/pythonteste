#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
n = input('Digite um nome :')
if 'Silva' in n.title():
    print("Seu nome tem 'Silva'")
else:
    print("Seu nome nao tem 'Silva'")

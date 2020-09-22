#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
n = input('Digite um nome :').title().strip()
print(f'Seu nome tem Silva ? : {"Silva" in n}')
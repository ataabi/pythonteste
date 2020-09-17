# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
import pyconverter
print('Conversor de Base')
n = int(input('Valor inteiro : '))
print('Para qual base deseja converter ?\n'
      '|1 - Binário | 2 - Octal | 3 - Hexadecimal|')
esc = int(input(': '))
dic = {1:'Binário',2:'Octal',3:'Hexadecimal'}

if esc == 1:
        conv = pyconverter.inttobin(n)
elif esc == 2:
        conv = pyconverter.bintooct(pyconverter.inttobin(n))
else:
        conv = pyconverter.inttohex(n)
print(f'{dic[esc]}: {conv}')


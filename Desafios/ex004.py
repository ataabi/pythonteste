# Façã um programa que leia algo pelo teclado emostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ela
tipos = input('Digite alguma coisa :')
print('O tipo primitivo desse valor é ', Type(a))
print('É alfanumerico ?',(tipos.isalnum()))
print('É alfabetico ?',(tipos.isalpha()))
print('É ASCII ?',(tipos.isascii()))
print('É decimal ?',(tipos.isdecimal()))
print('É um digito ?',(tipos.isdigit()))
print('É Identifier ?',(tipos.isidentifier()))
print('É Maiusculo ?',(tipos.isupper()))
print('É minusculo ?',(tipos.islower()))
print('É um número ?',(tipos.isnumeric()))
print('É printavel ?',(tipos.isprintable()))
print('So tem espaços ? ',(tipos.isspace()))
print('Esta capitalizada ? ',(tipos.istitle()))

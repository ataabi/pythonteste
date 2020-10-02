# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrálo por extenso.
alp = ('zero','um','dois','tres','quatro','cinco','sex','set','oito','nove','dez',
       'onze','doze','treze','quatorze','quinze','deszeseis','deszessete','dezoito','deszenove','vinte')
num = int(input('Digite um valor inteiro entre 0 e 20: '))
while not num in range(0,len(alp)):
    num = int(input('Valor Inválido, Tente novámente.\n'
                'Digite um valor inteiro entre 0 e 20: '))
print(f'Você digitou {alp[(num)]}')
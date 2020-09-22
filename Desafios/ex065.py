# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
l = []
m = c = 0
print('Média, Maior, Menor.')
while True:
    n = int(input('Digite um valor: '))
    esc = input('Continuar ? (S/N)').upper()
    l.append(n)
    m += n
    c += 1
    if esc == 'N':
        break
sorted(l)
print(f'A media é {m/c:.2f}')
print(f'Maior {l[0]}, Menor {l[-1]}')
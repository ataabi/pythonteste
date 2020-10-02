# Desenvolva um programa que leia o primeiro termo e a razão de uma pa.
# no final, mostre os 10 primeiros termos dessa progressão.
print('Verificador de PA.')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
f = ((r*10)+p1)
count = 1
for c in range(p1,f,r):
    print(f'P{count}:({c}),',end=' ')
    count += 1
print('Fim')

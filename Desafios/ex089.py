# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# pertima que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
print('-='*25)
print(f'{"Registro de Boletim":-^50}')
print('-='*25)

while True:
    alunos = [0,[0,0],0]
    alunos[0] = str(input('Nome: ')).strip().title()
    alunos[1][0] = float(input('1ª Nota: '))
    alunos[1][1] = float(input('2ª Nota: '))
    alunos[2] = ((alunos[1][0] + alunos[1][1])/2)
    boletim.append(alunos[:])
    esc = str(input('Deseja Continuar [S/N]: '))
    if esc in 'Nn':
        break
print('-='*25)
print(f'|{"Noº":^5}|{"Nome":^10}|{"Média":^9}|')
for e,c in enumerate(boletim):
    print(f'|{e:^5}|{boletim[e][0]:^10}|{boletim[e][2]:^9}|')
print('-='*25)

while esc != 999:
   esc = int(input('(Digite [999] para sair'
                   '\nExibir notas de qual aluno ? '))
   for e,c in enumerate(boletim):
       if e == esc:
           print(f'As notas de {boletim[e][0]} são {boletim[e][1]}')
   print('-='*25)
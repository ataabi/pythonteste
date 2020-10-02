lanche = ('Hambúrguer','Suco','Pizza','Pudim')
print(sorted(lanche))
print(lanche)

for c in lanche:
    print(f'Eu vou comer {c}')

for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

for p, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {p}')

print('Comi pra caralho')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5))

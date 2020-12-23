def soma(* valores):
    s = 0
    for n in valores:
        s += n
    print(f'A soma dos valores é {s}')


def contador(* num):
    print(len(num))


def dobra(l):
    pos = 0
    while pos <len(l):
        l[pos] *= 2
        pos += 1
    print(l)


# Programa principal
soma(2,3,4,1,2,3,5)
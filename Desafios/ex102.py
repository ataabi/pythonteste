# Crie um programa que que faça uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado
# ou não na tela o processo de cálculo de fatorial.

def fatorial(x, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param x: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """

    f = 1
    if show == True:
        for c in range(x, 0, -1):
            f *= c
            print(f'{c} x ',end='')
        print('= ',end='')
        return f
    if show == False:
        for c in range(x, 0, -1):
            f *= c
        return f

print(fatorial(5))
print('-='*20)
print(fatorial(5,show=True))
print('-='*20)
help(fatorial)





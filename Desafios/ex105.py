# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos. (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = {}
    med = 0
    for e,c in enumerate(n):
        med += c
        if e == 0:
            alunos["Maior"] = c
            alunos['Menor'] = c
        else:
            if c < alunos['Menor']:
                alunos['Menos'] = c
            if c > alunos['Maior']:
                alunos['Maior'] = c
    alunos['Média'] = med/(len(n))
    if sit == True:
        if med <= 5.4:
            alunos['Situação'] = 'RUIM'
        if med <= 6.9:
            alunos['Situação'] = 'RAZOÁVEL'
        if med >= 7:
            alunos['Situação'] = 'BOA'
        if med == 10:
            alunos['Situação'] = '* Perfeita *'
    return alunos



#MainBody
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
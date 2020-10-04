# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplivativo deverá analizar se a expressão passada está com os parênteses abertos e fechado na ordem correta.
'''
exp = input('Digite uma expressão:\n').strip()
if '(' not in exp or ')' not in exp:
    print('Essa não é uma expressão válida.')
elif exp.count('(') == exp.count(')'):
    print('Sua espressão esta com os parênteses corretos.')
elif exp.count('(') > exp.count(')'):
    print(f"Faltou abrir {exp.count('(') - exp.count(')')} ) na sua expressão")
elif exp.count('(') < exp.count(')'):
    print(f"Faltou fechar {exp.count(')') - exp.count('(')} ( na sua expressão")
'''

#respota

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
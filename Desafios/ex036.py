# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O Programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo sera negado.
print('Consulta de emprestimo bancário.')
vacasa = float(input('Qual o Valor da Casa ? R$'))
salario = float(input('Qual o Salário do comprador ? R$'))
anos = int(input('Em quantos anos vai ser pago ? : '))
men = vacasa/(anos*12)
if men > (salario*0.30):
    print(f'Desculpe, mas seu salario é de R${salario} e a mensalidade vai fica em {men:.2f}\n'
          f'entao nao poderemos aprovar seu empréstimo.')
elif men < (salario*0.30):
    print(f'Parabéns. Seu empréstimo foi aprovado.\n'
          f'você ira pagar {anos*12:.0f} prestações de R${men:.2f}.')

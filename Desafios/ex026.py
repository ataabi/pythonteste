#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes apparece a letra "A"
# Em que posiçao pela aparece a primeira vez.
#Em que posição ela aparece a ultima vez.
n = 'n1 a2 a3 a4' #input('Digite uma frase :\n')
print(f'''Essa Frase possui {n.upper().count('A')} 'A' ''')
print(f"Aparece primeiro na posicaão {n.upper().find('A')}\n"
      f"e Por ultimo na posição {n.upper().rfind('A'):}")
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes apparece a letra "A"
# Em que posiçao pela aparece a primeira vez.
#Em que posição ela aparece a ultima vez.
print("Quantos 'A' tem na Frase ?")
n = input('Digite uma frase : ').upper().strip()
print(f"A letra 'A' aparece {n.count('A')}x\n"
      f"O primeiro 'A' aparece na posicaão {n.find('A')+1}\n"
      f"E o ultimo 'A' aparece na posição posição {n.rfind('A')+1:}")
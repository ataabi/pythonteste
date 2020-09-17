# Faça um programa que leia um angulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse angulo
import math
ang = float(input('Digite o ângulo : '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'Ângulo   : {ang}°.\n'
       f'Seno     : {sen:.2f}\nCosseno  : {cos:.2f}\nTangente : {tan:.2f}')

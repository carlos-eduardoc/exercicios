"""
Faça um programa que leia um número e exiba a tabuada completa dele (de 1 a 10), 
mostrando a operação formatada em cada linha.
Digite um número: 7 7 x 1 = 7 7 x 2 = 14 ... 7 x 10 = 70
"""

numero_b = int(input('Digite um numero base para mostrar a tabauda: '))

for i in range(1, 11):
    print(f'{numero_b} x {i} = {numero_b * i}')
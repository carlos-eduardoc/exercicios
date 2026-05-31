"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
 mostre a listagem de números gerados e 
também indique o menor e o maior valor que estão na tupla.
"""

from random import randint as rint

num = (rint(1, 10),  rint(1, 10), rint(1, 10), rint(1, 10), rint(1, 10))

for n in num:
    print(f'Os numeros gerados foram: {n}')

print(f'O maior numero entre eles foi o: {max(num)}')
print(f'O menor numero entre eles foi o: {min(num)}')
    

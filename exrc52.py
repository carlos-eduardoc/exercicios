"""
Faça um programa que leia um número N e exiba os N primeiros termos da sequência de Fibonacci.
 Cada termo é a soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8...).
Quantos termos? 8 0 1 1 2 3 5 8 13
"""

term = int(input('Digite quantos termos: '))

a = 0
b = 1

for t in range(term):
   print(a)
   proximo = a + b
   b = proximo


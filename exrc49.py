"""
Faça um programa que leia um número inteiro positivo e calcule o seu fatorial usando 
for. Não use bibliotecas, só o laço.
Digite um número: 5 5! = 120 (5x4x3x2x1)
"""

num = int(input('Digite um numero: '))

resultado = 1

for n in range(1, num + 1):
  resultado *= n
  print(f'Fatorial do {num} é de {resultado}')
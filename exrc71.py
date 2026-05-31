"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

Aula Anterior

"""

num = int(input('Digite qualquer numero: '))
resultado = 1

while num > 1:
    resultado *= num
    num -= 1

print(resultado)
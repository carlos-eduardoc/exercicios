"""
Faça um programa que leia dois números inteiros e calcule a soma de todos os inteiros entre eles
 (inclusive os dois extremos).
Digite o primeiro número: 3 Digite o segundo número: 7 Soma de 3 até 7 = 25 (3+4+5+6+7)
"""

num1 = int(input('Digite um numero: '))
num2 = int(input('Outro numero: '))
total = 0

for n in range(num1, num2 + 1):
    total += n

    print(f'O factorial de soma do numero {num1} até {num2} é de {total}')
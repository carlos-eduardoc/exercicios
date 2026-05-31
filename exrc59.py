"""
Leia N números e exiba quantos são positivos, negativos e zeros.
"""

n = int(input('Quantos numeros: '))

positivos = 0
negativos = 0
zeros = 0

for i in range(n):
    num = int(input('Digite um numero: '))

    if num < 0:
        negativos += 1
    if num > 0:
        positivos += 1
    if num == 0:
        zeros += 1
print(f'TEM quantos: \n POSITIVOS: {positivos} \n NEGATIVOS: {negativos} \n ZEROS: {zeros}')
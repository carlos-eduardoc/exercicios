"""
Leia N números e exiba a soma apenas dos números pares.
"""

n = int(input('Quantos numeros: '))

soma_par = 0

for i in range(n):
    num = int(input('Digite um numero: '))

    if num % 2 == 0:
        soma_par += num
    
print(f'A soma dos numeros pares é de {soma_par}')
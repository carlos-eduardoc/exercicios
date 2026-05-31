"""
Leia N números e conte quantos são pares e quantos são ímpares.

"""

n = int(input('QUantos numeros: '))
par = 0
impar = 0

for i in range(n):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Tem {par} pares e {impar} impares!')

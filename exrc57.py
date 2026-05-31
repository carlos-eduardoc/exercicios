"""
Leia N números e exiba a soma e o produto de todos eles.Você
 disse: produto seria resultado na multiplicação
"""

n = int(input('Digite quantos numeros: '))

soma = 0
multi = 1

for nuns in range(n):
    numero = int(input('Digite um numero: '))
    soma += numero
    multi *= numero
    
print(f'A soma é de {soma}')
print(f'A multiplicação é de {multi}')
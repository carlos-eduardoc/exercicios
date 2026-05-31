"""
Leia N números e exiba a média apenas dos números ímpares.
"""

n = int(input('Quantos numeros: '))

qntd_impar = 0
soma_impar = 0

for i in range(n):
    num = int(input('Digite um numero: '))

    if num % 2 != 0:
        soma_impar += num
        qntd_impar += 1

if qntd_impar == 0:
    print('Digite algum impar!')
else:
    print(f'A soma dos numeros impares são {soma_impar} e a media é {soma_impar / qntd_impar}')
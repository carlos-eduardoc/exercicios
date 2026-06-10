"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
 A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint 

numeros = []

def sorteia():
    for i in range(6):
        numero_sort = randint(1, 100)
        numeros.append(numero_sort)

    print('Os numeros sorteados foram: ', *numeros)

def somaPar():
    soma = 0

    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma entre os numeros pares é {soma}')

sorteia()
somaPar()
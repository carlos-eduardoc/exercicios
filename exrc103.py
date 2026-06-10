"""
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep as sl

def maior(*numeros):
    maior = 0
    
    print('Analisando valores..')
    for n in numeros:
        print(f'{n} ', end='', flush=True)
        sl(0.25)

        if n > maior:
            maior = n

    print(f'...Os valores foram as analisados, e o maior entre eles foi o {maior}')

maior(1, 2, 3, 7, 2
, 3, 1000, 23, 261)
maior(1, 2, 10, 13, 12, 177)
maior(6, 7, 8, 22, 11)
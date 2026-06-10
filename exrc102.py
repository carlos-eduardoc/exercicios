"""""""""""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada: 

a) de 1 até 10, de 1 em 1        b) de 10 até 0, de 2 em 2              c) uma contagem personalizada
"""""""""""
from time import sleep as dorme

def contador(inicio, fim, passo):

    for n in range(inicio, fim, passo):
        dorme(0.25)
        print(f'{n}..')

contador(1, 11, 1)
contador(10, -1, -2)

print('Personalize sua contagem')

ini = int(input('POr onde ela começa: '))
para = int(input('Onde ela para: '))
coelho = int(input('Pula de quanto em quanto (1 em 1.. 2 em 2..etc): '))

contador(ini, para, coelho)
"""
Faça um programa que leia um número inicial, um número final e um passo. b
Exiba todos os números desse intervalo pulando de acordo com o passo informado.
Digite o início: 2 Digite o fim: 20 Digite o passo: 3 → 2 5 8 11 14 17 20

"""
from time import sleep as sl

start_n = int(input('Digite o numero para começar a contagem: '))
stop_n = int(input('Digite o numero que a conatagem deve parar: '))
step_n = int(input('Digite o umero que a contagem deve ir pulando (ex: de 2 em 2): '))

for n in range(start_n, stop_n, step_n):
    print(n)
    sl(1.0)
    